<template>
    <div class="draws-container">
        <h2>Recent Draws</h2>
        <div class="draw-list">
            <div v-for="draw in draws" :key="draw.id" class="draw-box">
                <h3>{{ formatDate(draw.date) }}</h3>
                <ul>
                    <li v-for="participant in draw.participants" :key="participant.id">
                        {{ participant.giver.name }} is giving to {{ participant.receiver.name }}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
.draws-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* Center-align items vertically */
    padding: 20px;
}

.draw-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px; /* Space between boxes */
    justify-content: center; /* Center-align the boxes horizontally */
}

.draw-box {
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    width: 300px; /* Fixed width for each draw box */
}

h2, h3 {
    margin: 10px 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    padding: 5px 0;
}
</style>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            draws: []
        };
    },
    methods: {
        async fetchDraws() {
            try {
                const response = await axios.get('http://localhost:8000/api/draws/');
                this.draws = response.data;
            } catch (error) {
                console.error('Error fetching draws:', error);
            }
        },
        formatDate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString(undefined, {
                year: 'numeric', month: 'long', day: 'numeric',
                hour: '2-digit', minute: '2-digit'
            });
        }
    },
    created() {
        this.fetchDraws();
    }
}
</script>
