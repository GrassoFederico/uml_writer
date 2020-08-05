<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Accelerator extends Model
{
    protected $fillable = ['payment_type_id', 'product_id', 'offer_id'];

    protected $hidden = ['payment_type_id', 'product_id', 'offer_id'];

    public function payment_type()
    {
        return $this->belongsTo('\App\PaymentType', 'payment_type_id');
    }

    public function product()
    {
        return $this->belongsTo('\App\Product');
    }

    public function offer()
    {
        return $this->belongsTo('\App\Offer', 'offer_id');
    }
}
