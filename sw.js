const CACHE_NAME = 'chaodp-v1.0.0';
const urlsToCache = [
  '/',
  '/css/main.css',
  '/js/main.js',
  '/images/logo.png',
  '/images/hero-image.jpg',
  '/fonts/PingFangSC-Regular.woff2',
  '/shenzhen-ruanzhuang-design-landing-page.html'
];

// 安装Service Worker
self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// 拦截网络请求
self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        // 如果缓存中有响应，则返回缓存的版本
        if (response) {
          return response;
        }

        // 否则从网络获取
        return fetch(event.request).then(
          function (response) {
            // 检查是否收到有效响应
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // 克隆响应
            var responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(function (cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
  );
});

// 清理旧缓存
self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (cacheNames) {
      return Promise.all(
        cacheNames.map(function (cacheName) {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});