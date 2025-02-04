[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Viewpoint<T0>

class in UnityEditor

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Defines a Viewpoint that can be selected from the Cameras overlay.

Use this base class with [ICameraLensData](ICameraLensData.html) to define a
Viewpoint and expose a component in the Cameras overlay. If you expose a
component in the Cameras overlay, you can use the Cameras overlay to look
through that component in the Scene view.  
  
To use this class, you must have a custom representation of your camera lens
in a [MonoBehaviour](MonoBehaviour.html).  
  
When detected, the Cameras overlay creates an instance of the Viewpoint class
for each component that is type T0 in the scene.  
  
The Cameras overlay uses the icon that is attached to the component in the UI.

    
    
    using UnityEngine;  
      
    public class MyVirtualCamera : [MonoBehaviour](MonoBehaviour.html)
    {
        public float fov;
        public float nearPlane;
        public float farPlane;  
      
        public bool physicalProps;
        public float focalLength;
        public [Vector2](Vector2.html) sensor;
        public [Vector2](Vector2.html) lensShift;
        public [Camera.GateFitMode](Camera.GateFitMode.html) gateFit;
    }
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class VirtualCameraViewpoint : Viewpoint<MyVirtualCamera>, [ICameraLensData](ICameraLensData.html)
    {
        public VirtualCameraViewpoint(MyVirtualCamera target) : base(target) { }  
      
        public float NearClipPlane => Target.nearPlane;  
      
        public float FarClipPlane => Target.farPlane;  
      
        // If you are not using physical properties, FieldOfView can change from the [SceneView](SceneView.html) with the scrollwheel action while looking through a camera.
        public float FieldOfView { get => Target.fov; set => Target.fov = value; }  
      
        public bool UsePhysicalProperties => Target.physicalProps;  
      
        // If you are using physical properties, FocalLength can change from the [SceneView](SceneView.html) with the scrollwheel action while looking through a camera.
        public float FocalLength { get => Target.focalLength; set => Target.focalLength = value; }  
      
        public [Vector2](Vector2.html) SensorSize => Target.sensor;  
      
        public [Vector2](Vector2.html) LensShift => Target.lensShift;  
      
        public [Camera.GateFitMode](Camera.GateFitMode.html) GateFit => Target.gateFit;  
      
        // The [SceneView](SceneView.html) sets orthographic to true when: 
        // - the 2DMode button is toggled on.
        // - orthographic view is set from the [Orientation](Experimental.GraphView.Orientation.html) gizmo.
        //
        // In this example, our representation doesn't consider orthographic view.
        public bool Orthographic { get => false; set { } }
        public float OrthographicSize { get => 0; set { } }
    }

### Properties

[Position](Viewpoint_1.Position.html)| The world position.  
---|---  
[Rotation](Viewpoint_1.Rotation.html)| The world rotation.  
[Target](Viewpoint_1.Target.html)| Returns the component the Viewpoint is
attached to cast as T.  
[TargetObject](Viewpoint_1.TargetObject.html)| A reference to the Component of
type T this Viewpoint is attached to.  
  
### Constructors

[Viewpoint_1](Viewpoint_1-ctor.html)| Constructor.  
---|---  
  
### Public Methods

[CreateVisualElement](Viewpoint_1.CreateVisualElement.html)|
CreateVisualElement is called when a Viewpoint is selected in the Cameras
Overlay.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

