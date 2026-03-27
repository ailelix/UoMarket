<template>
  <nav class="bg-white shadow-md border-b border-gray-100 w-full drop-shadow-xl">
    <div class="max-w-8xl mx-auto px-12">
      <div class="flex items-center h-24 px-4 sm:px-6 lg:px-8 py-4">
        <div class="flex-1 flex items-center">
          <a href="/" class="text-4xl font-extrabold tracking-tight hover:opacity-80 transition">
            <span class="text-uom-purple">UOM</span><span class="text-uom-yellow">ARKET</span>
          </a>
        </div>

        <div class="flex-1 flex justify-center items-center">
          <router-link to="/marketplace" class="marketplace-btn">
            Marketplace
          </router-link>
        </div>

        <div class="flex-1 flex justify-end items-center text-lg font-bold">
          <template v-if="user">
            <router-link to="/profile" class="login-btn">
              Profile
            </router-link>
            <button @click="logout" class="ml-4 text-sm font-medium text-slate-600 hover:text-slate-900 transition underline">
              Logout
            </button>
          </template>
          <template v-else>
            <router-link to="/login" class="login-btn">
              Login
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const user = ref(null);

onMounted(async () => {
  try {
    const res = await axios.get('/api/me');
    user.value = res.data;
  } catch (err) {
    user.value = null;
  }
});

const logout = async () => {
  try {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    await axios.post('/api/logout');
    window.location.href = '/';
  } catch (err) {
    console.error(err);
  }
};
</script>

<style scoped>
.marketplace-btn {
  background: linear-gradient(135deg, #660099 0%, #9933cc 100%);
  color: white;
  padding: 0.75rem 2rem;
  border-radius: 9999px; /* Pill shape */
  font-weight: 800;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(102, 0, 153, 0.4);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  position: relative;
  overflow: hidden;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 1rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.marketplace-btn:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(102, 0, 153, 0.6);
  background: linear-gradient(135deg, #7a00b8 0%, #aa3ee0 100%);
}

.marketplace-btn:active {
  transform: translateY(-1px) scale(0.98);
  box-shadow: 0 4px 10px rgba(102, 0, 153, 0.4);
}

/* Shine effect */
.marketplace-btn::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: 0.5s;
}

.marketplace-btn:hover::after {
  left: 100%;
  transition: 0.7s ease-in-out;
}

/* New Login Button Styles */
.login-btn {
  background: white;
  color: #660099;
  border: 2px solid #e5e7eb;
  padding: 0.6rem 1.75rem;
  border-radius: 9999px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  position: relative;
  overflow: hidden;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.login-btn:hover {
  border-color: #660099;
  background: #f9fafb;
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 4px 12px rgba(102, 0, 153, 0.1);
  color: #4d0073;
}

.login-btn:active {
  transform: translateY(0) scale(0.98);
}

/* Subtle shine effect */
.login-btn::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(102, 0, 153, 0.1),
    transparent
  );
  transition: 0.5s;
}

.login-btn:hover::after {
  left: 100%;
  transition: 0.7s ease-in-out;
}
</style>
