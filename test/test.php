<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Validation\Rule;
use App\Repositories\Payments\PayPal\Response;
use App\Repositories\Payments\RemoteController;
use App\Repositories\Payments\Device;
use App\Repositories\Facade\Invoice;
use App\Repositories\Facade\Offer;
use App\Events\OrderCompleted;
use App\PaymentType;
use App\PaymentTransition;
use App\Events\AddressUpdated;

class PaymentController extends Controller
{
    private $order;
    private $remote_controller;
    private $payment_identifier;
    private $payer_identifier;

    public function create(Request $request)
    {
        $this->init_components($request);

        if($request->error)
            return redirect()->back()->withErrors(['pay' => $request->error]);
        else
            return redirect()->away($this->remote_controller->get_payment_link());
    }

    public function return(Request $request)
    {
        $this->init_components($request);

        if(empty($this->payment_identifier))
            return back();

        $registry = $this->remote_controller->get_payer_info( $this->payment_identifier );
        return view('pages.pay', ['registry' => $registry]);
    }

    public function execute(Request $request)
    {
        $this->init_components($request);

        event(new AddressUpdated($this->order, $request));

        if(empty($this->payment_identifier) || empty($this->payer_identifier))
            return back();

        $result = $this->remote_controller->get_payment_result( $this->payment_identifier, $this->payer_identifier );
        $state = strtoupper($result->state);

        if(($state === config('order.status.completed')) || ($state === config('order.status.pending')))
        {
            event(new OrderCompleted($this->order));
            return redirect()->route('thankyou');
        }
        elseif( $result->state === Response::NO_FUNDS )
            return redirect()->away($this->remote_controller->get_payment_link($this->payment_identifier));
        else
            return redirect()->route('checkout')->withErrors(['pay' => $result->error]);
    }

    public function cancel(Request $request)
    {
        return redirect()->route('checkout')->withErrors([
            'pay' => __('payments.cancel')
        ]);
    }

    private function init_components(Request $request): void
    {
        $request->validate([
            'payment' => ['required', 'string', Rule::in(config('payments.available'))]
        ]);

        $this->order = \App\Order::find( session('order_id') );
        
        $this->init_payment_transition( $this->get_payment_type($request->payment) );
        $this->offer = Offer::build($this->order);
        $this->invoice = Invoice::build($this->order);

        $this->remote_controller = new RemoteController( $this->get_payment_device( $request ) );
    }

    private function init_payment_transition(PaymentType $payment_type): void
    {
        PaymentTransition::updateOrCreate([
                'order_id' => $this->order->id
            ], [
                'payment_type_id' => $payment_type->description,
                'amount' => $this->order->order_total
            ]);
    }

    private function get_payment_type(string $payment_type_description): PaymentType
    {
        return PaymentType::find($payment_type_description) ?? PaymentType::find( config('payments.default') );
    }

    private function get_payment_device(Request $request)
    {
        if($request->payment === 'PAYPAL')
        {
            $this->payer_identifier = $request->PayerID;
            $this->payment_identifier = $request->paymentId;

            return new \App\Repositories\Payments\PayPalDevice( $this->invoice );
        }
        else
        {
            $this->payer_identifier = $this->order->id;
            $this->payment_identifier = $this->order->id;

            return new \App\Repositories\Payments\CashOnDeliveryDevice;
        }
    }
}
