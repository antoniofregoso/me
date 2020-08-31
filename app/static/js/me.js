const objs = document.querySelectorAll('[data-animation]');
var observer = new IntersectionObserver(function(entries) {
	entries.forEach(entry => {
		animation = 'animate__'.concat(entry.target.dataset.animation);
		if (entry.intersectionRatio > 0) {
			entry.target.classList.add('animate__animated',  animation);
		} else {
			entry.target.classList.remove('animate__animated',  animation);
			}
		});
			});
	objs.forEach(obj => {
		observer.observe(obj);
});	