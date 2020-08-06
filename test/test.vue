<template>
    <div class="container table-responsive">
        <table class="table table-striped table-hover">
            <thead class="thead-dark">
                <tr>
                    <th v-for="header in headers" :key="header" scope="col">
                        {{ translation[header] }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="value in data" :key="getValueId(value)" @click="redirectTo(`/${route}/${getValueId(value)}`)">
                    <td v-for="(val, index) in value" :key="val + index">
                        <img v-if="isPath(index)" :src="`storage/${val}`" :alt="val"
                            class="img-fluid w-25">
                        <span v-else>{{ val }}</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        computed: {
            headers: function() {
                return Object.keys(this.data[0]);
            }
        },
        methods: {
            redirectTo: function(url) {
                window.location.href = url;
            },
            isPath: function(value) {
                return this.paths != undefined ? this.paths.includes(value) : false;
            },
            getValueId: function(value) {
                return this.id != undefined ? value[this.id] : value.id;
            }
        },
        props: ['route', 'data', 'paths', 'id', 'translation']
    }
</script>

<style lang="scss" scoped>

    a {
        text-decoration: none;
    }

    .table-hover {

        tbody {

            tr {
                cursor: pointer;
            }
        }
    }

</style>
