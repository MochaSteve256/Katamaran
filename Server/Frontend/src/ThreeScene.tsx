import React, { useRef } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { Mesh } from "three";

type Rotation = [number, number, number];

interface ThreeSceneProps {
  rotation: Rotation;
}

const ThreeScene: React.FC<ThreeSceneProps> = ({ rotation }) => {
  const boxRef = useRef<Mesh>(null); // Define the type of ref explicitly

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        position: "relative", // Ensure correct positioning
        overflow: "hidden",
      }}
    >
      <Canvas
        style={{
          position: "absolute", // Position canvas absolutely
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
        }}
      >
        <gridHelper args={[4, 4]} />
        <ambientLight />
        <directionalLight position={[10, 10, 10]} intensity={10} />
        <mesh ref={boxRef} rotation={rotation}>
          <boxGeometry args={[1, 0.5, 1]} />
          <meshStandardMaterial color="orange" />
        </mesh>
        <OrbitControls enableZoom={false} />
      </Canvas>
    </div>
  );
};

export default ThreeScene;
