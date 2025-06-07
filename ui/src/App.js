import React from 'react';
import maplibregl from 'maplibre-gl';
import axios from 'axios';

export default function App() {
  React.useEffect(() => {
    const map = new maplibregl.Map({
      container: 'map',
      style: 'https://demotiles.maplibre.org/style.json',
      center: [-53.75, -11.57], zoom: 6
    });
    return () => map.remove();
  }, []);

  return (
    <div style={{display:'flex',height:'100vh'}}>
      <div id='map' style={{flex:1}} />
      <div style={{width:300,padding:10}}>
        <h2>AOI Explorer</h2>
      </div>
    </div>
  );
}
