<template>
    <div v-if="isVisible" class="modal">
        <div class="modal-content">
            <span class="close" @click="closeModal">&times;</span>
            <h3>Manage Blacklist for {{ currentParticipant.name }}</h3>
            <div v-if="message.content" :class="`message ${message.type}`">{{ message.content }}</div>
           <select v-model="localParticipant.blacklist" multiple>
                <option v-for="other in participants" :key="other.id" :value="other.id" :disabled="other.id === localParticipant.id">
                    {{ other.name }}
                </option>
            </select>
            <button @click="updateBlacklist">Update Blacklist</button>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    props: ['participants', 'currentParticipant', 'isVisible'],
    data() {
        return {
            localParticipant: this.deepCopyParticipant(this.currentParticipant),
            message: {
                content: '',
                type: ''  // 'success' or 'error'
            }
        };
    },
    methods: {
        deepCopyParticipant(participant) {
            return JSON.parse(JSON.stringify(participant));
        },
        closeModal() {
            this.$emit('close');
            this.message = { content: '', type: '' };  // Reset message when closing modal
        },
        async updateBlacklist() {
            try {
                const blacklistUpdates = this.localParticipant.blacklist.map(blockedId => axios.post('http://localhost:8000/api/blacklists/', {
                    participant: this.localParticipant.id,
                    cannot_receive_from: blockedId
                }));
                await Promise.all(blacklistUpdates);
                this.message = { content: 'Blacklist updated successfully', type: 'success' };
                this.$emit('blacklist-updated', this.localParticipant);
            } catch (error) {
                console.error('Error updating blacklist:', error);
                this.message = { content: 'Error updating blacklist', type: 'error' };
            }
        }
    },
    watch: {
        currentParticipant: {
            handler(newValue) {
                this.localParticipant = this.deepCopyParticipant(newValue);
            },
            deep: true,
            immediate: true
        }
    }
};
</script>


<style>
.modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

.message {
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
    text-align: center;
    color: #fff;
}

.success {
    background-color: #4CAF50;
}

.error {
    background-color: #f44336;
}

</style>
