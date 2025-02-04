[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CameraRays-cast.html)
  * [中文](/cn/current/Manual/CameraRays-cast.html)
  * [日本語](/ja/current/Manual/CameraRays-cast.html)
  * [한국어](/kr/current/Manual/CameraRays-cast.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CameraRays-cast.html)
  * [中文](/cn/current/Manual/CameraRays-cast.html)
  * [日本語](/ja/current/Manual/CameraRays-cast.html)
  * [한국어](/kr/current/Manual/CameraRays-cast.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [The camera view](CameraView.html)
  * [Rays from the camera](CameraRays.html)
  * Cast a ray from a camera

[](CameraRays-introduction.html)

Introduction to raycasting

[](CameraRays-move.html)

Move a camera along a ray

# Cast a ray from a camera

The most common use of a Ray from the **camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) is to perform a
[raycast](../ScriptReference/Physics.Raycast.html) out into the **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). A raycast sends an imaginary “laser
beam” along the ray from its origin until it hits a **collider** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) in the scene. Information is then
returned about the object and the point that was hit in a
[RaycastHit](../ScriptReference/RaycastHit.html) object. This is a very useful
way to locate an object based on its onscreen image. For example, the object
at the mouse position can be determined with the following code:

    
    
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        public Camera camera;
    
        void Start(){
            RaycastHit hit;
            Ray ray = camera.ScreenPointToRay(Input.mousePosition);
            
            if (Physics.Raycast(ray, out hit)) {
                Transform objectHit = hit.transform;
                
                // Do something with the object that was hit by the raycast.
            }
        }
    }
    

[](CameraRays-introduction.html)

Introduction to raycasting

[](CameraRays-move.html)

Move a camera along a ray

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

