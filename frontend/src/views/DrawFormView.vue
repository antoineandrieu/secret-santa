<template>
    <div>
        <h1>Create a Draw</h1>
        <button @click="createDraw">Create Draw</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    methods: {
        async createDraw() {
            try {
                const response = await axios.post('http://localhost:8000/api/draws/');
                console.log(response);
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>
