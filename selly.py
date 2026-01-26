import React, { useState, useEffect } from 'react';
import FallingHearts from './components/FallingHearts';

const App: React.FC = () => {
  const [showCelebration, setShowCelebration] = useState(false);
  const [showToast, setShowToast] = useState(false);

  // Generic flowers image URL
  const flowersUrl = "https://images.unsplash.com/photo-1561181286-d3fee7d55364?q=80&w=800&auto=format&fit=crop";

  const handleButtonClick = () => {
    setShowCelebration(true);
    setShowToast(true);
  };

  useEffect(() => {
    if (showToast) {
      const timer = setTimeout(() => {
        setShowToast(false);
      }, 3000); // Hide toast after 3 seconds
      return () => clearTimeout(timer);
    }
  }, [showToast]);

  return (
    <div className="min-h-screen bg-black flex flex-col items-center justify-center p-4 gap-8 relative overflow-hidden font-sans">
      
      {/* Spacer equivalent to <br><br> */}
      <div className="h-8"></div>

      {/* Button */}
      <div className="z-10">
        <button
          onClick={handleButtonClick}
          className={`
            bg-[#FF1493] text-white 
            border-none 
            py-[18px] px-[50px] 
            text-[28px] font-bold 
            rounded-[50px] 
            shadow-[0px_0px_20px_#FF1493] 
            transition-all duration-300 
            hover:scale-110 hover:shadow-[0px_0px_35px_#FF1493]
            active:scale-95
            cursor-pointer
          `}
        >
          Hey Selly
        </button>
      </div>

      {/* Celebration Text */}
      {showCelebration && (
        <div className="animate-pulse">
           <h1 className="text-[#FF1493] text-4xl md:text-5xl font-bold text-center mt-4">
             ❤️ SELLY ❤️
           </h1>
        </div>
      )}

      {/* Image */}
      <div className="mt-4">
        <img 
          src={flowersUrl} 
          alt="Flowers" 
          className="rounded-[15px] shadow-[0px_0px_10px_rgba(255,255,255,0.1)] max-w-full w-[600px] object-cover"
        />
      </div>

      {/* Toast Notification */}
      {showToast && (
        <div className="fixed top-10 bg-white/10 backdrop-blur-md border border-pink-500/30 text-white px-6 py-3 rounded-xl shadow-lg animate-bounce z-50">
           💖💖💖💖💖
        </div>
      )}

      {/* Falling Hearts Effect (Simulating st.snow) */}
      {showCelebration && <FallingHearts />}
    </div>
  );
};

export default App;
