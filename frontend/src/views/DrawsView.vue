<template>
    <div>
        <h1>Recent Draws</h1>
        <ul>
            <li v-for="draw in draws" :key="draw.id">
                Draw ID: {{ draw.id }} - Date: {{ draw.date }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            draws: []
        };
    },
    async created() {
        try {
            const response = await axios.get('http://localhost:8000/api/draws/');
            this.draws = response.data;
        } catch (error) {
            console.error(error);
        }
    }
}
</script>
