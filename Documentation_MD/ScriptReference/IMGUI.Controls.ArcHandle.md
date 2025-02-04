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

# ArcHandle

class in UnityEditor.IMGUI.Controls

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

A class for a compound handle to edit an angle and a radius in the Scene view.

![](../StaticFiles/ScriptRefImages/ArcHandle.png) _ArcHandle in the Scene
View._  
  
This class allows you to display control handles for editing the angle and
radius of an arc. The arc originates at
[Vector3.forward](Vector3-forward.html) multiplied by the
[radius](IMGUI.Controls.ArcHandle-radius.html) and rotates around
[Vector3.up](Vector3-up.html). The handle rendered by this class's
[DrawHandle](IMGUI.Controls.ArcHandle.DrawHandle.html) method is affected by
global state in the [Handles](Handles.html) class, such as
[Handles.matrix](Handles-matrix.html) and [Handles.color](Handles-color.html).  
  
The following component defines an object with an angle and force property.

    
    
    using UnityEngine;  
      
    public class ProjectileExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float elevationAngle { get { return m_ElevationAngle; } set { m_ElevationAngle = value; } }
        [[SerializeField](SerializeField.html)]
        float m_ElevationAngle = 45f;  
      
        public float impulse { get { return m_Impulse; } set { m_Impulse = value; } }
        [[SerializeField](SerializeField.html)]
        float m_Impulse = 20f;  
      
        public [Vector3](Vector3.html) facingDirection
        {
            get
            {
                [Vector3](Vector3.html) result = transform.forward;
                result.y = 0f;
                return result.sqrMagnitude == 0f ? [Vector3.forward](Vector3-forward.html) : result.normalized;
            }
        }  
      
        protected virtual void Start()
        {
            [GameObject](GameObject.html) ball = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));  
      
            [Vector3](Vector3.html) direction = facingDirection;
            direction = [Quaternion.AngleAxis](Quaternion.AngleAxis.html)(elevationAngle, [Vector3.Cross](Vector3.Cross.html)(direction, [Vector3.up](Vector3-up.html))) * direction;
            ball.AddComponent<[Rigidbody](Rigidbody.html)>().AddForce(direction  * impulse, [ForceMode.Impulse](ForceMode.Impulse.html));
        }
    }
    

The following Custom Editor example allows you to edit the elevation angle and
force properties for this component in the Scene view, where the force is
represented by the radius of the handle.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.IMGUI.Controls;
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ProjectileExample))]
    public class ProjectileExampleEditor : [Editor](Editor.html)
    {
        [ArcHandle](IMGUI.Controls.ArcHandle.html) m_ArcHandle = new [ArcHandle](IMGUI.Controls.ArcHandle.html)();  
      
        protected virtual void OnEnable()
        {
            // arc handle has no radius handle by default
            m_ArcHandle.SetColorWithRadiusHandle([Color.white](Color-white.html), 0.1f);
        }  
      
        // the OnSceneGUI callback uses the [Scene](SceneManagement.Scene.html) view camera for drawing handles by default
        protected virtual void OnSceneGUI()
        {
            ProjectileExample projectileExample = (ProjectileExample)target;  
      
            // copy the target object's data to the handle
            m_ArcHandle.angle = projectileExample.elevationAngle;
            m_ArcHandle.radius = projectileExample.impulse;  
      
            // set the handle matrix so that angle extends upward from target's facing direction along ground
            [Vector3](Vector3.html) handleDirection = projectileExample.facingDirection;
            [Vector3](Vector3.html) handleNormal = [Vector3.Cross](Vector3.Cross.html)(handleDirection, [Vector3.up](Vector3-up.html));
            [Matrix4x4](Matrix4x4.html) handleMatrix = [Matrix4x4.TRS](Matrix4x4.TRS.html)(
                projectileExample.transform.position,
                [Quaternion.LookRotation](Quaternion.LookRotation.html)(handleDirection, handleNormal),
                [Vector3.one](Vector3-one.html)
            );  
      
            using (new [Handles.DrawingScope](Handles.DrawingScope.html)(handleMatrix))
            {
                // draw the handle
                [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
                m_ArcHandle.DrawHandle();
                if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                {
                    // record the target object before setting new values so changes can be undone/redone
                    [Undo.RecordObject](Undo.RecordObject.html)(projectileExample, "Change Projectile Properties");  
      
                    // copy the handle's updated data back to the target object
                    projectileExample.elevationAngle = m_ArcHandle.angle;
                    projectileExample.impulse = m_ArcHandle.radius;
                }
            }
        }
    }
    

Additional resources: [Editor.OnSceneGUI](Editor.OnSceneGUI.html),
[Handles.SetCamera](Handles.SetCamera.html).

### Properties

[angle](IMGUI.Controls.ArcHandle-angle.html)| Returns or specifies the angle
of the arc for the handle.  
---|---  
[angleHandleColor](IMGUI.Controls.ArcHandle-angleHandleColor.html)| Returns or
specifies the color of the angle control handle.  
[angleHandleDrawFunction](IMGUI.Controls.ArcHandle-
angleHandleDrawFunction.html)| The CapFunction to use when displaying the
angle control handle.  
[angleHandleSizeFunction](IMGUI.Controls.ArcHandle-
angleHandleSizeFunction.html)| The SizeFunction to specify how large the angle
control handle should be.  
[fillColor](IMGUI.Controls.ArcHandle-fillColor.html)| Returns or specifies the
color of the arc shape.  
[radius](IMGUI.Controls.ArcHandle-radius.html)| Returns or specifies the
radius of the arc for the handle.  
[radiusHandleColor](IMGUI.Controls.ArcHandle-radiusHandleColor.html)| Returns
or specifies the color of the radius control handle.  
[radiusHandleDrawFunction](IMGUI.Controls.ArcHandle-
radiusHandleDrawFunction.html)| The CapFunction to use when displaying the
radius control handle.  
[radiusHandleSizeFunction](IMGUI.Controls.ArcHandle-
radiusHandleSizeFunction.html)| The SizeFunction to specify how large the
angle control handle should be.  
[wireframeColor](IMGUI.Controls.ArcHandle-wireframeColor.html)| Returns or
specifies the color of the curved line along the outside of the arc.  
  
### Constructors

[ArcHandle](IMGUI.Controls.ArcHandle-ctor.html)| Creates a new instance of the
ArcHandle class.  
---|---  
  
### Public Methods

[DrawHandle](IMGUI.Controls.ArcHandle.DrawHandle.html)| A function to display
this instance in the current handle camera using its current configuration.  
---|---  
[SetColorWithoutRadiusHandle](IMGUI.Controls.ArcHandle.SetColorWithoutRadiusHandle.html)|
Sets angleHandleColor, wireframeColor, and fillColor to the same value, where
fillColor will have the specified alpha value. radiusHandleColor will be set
to Color.clear and the radius handle will be disabled.  
[SetColorWithRadiusHandle](IMGUI.Controls.ArcHandle.SetColorWithRadiusHandle.html)|
Sets angleHandleColor, radiusHandleColor, wireframeColor, and fillColor to the
same value, where fillColor will have the specified alpha value.  
  
### Static Methods

[DefaultAngleHandleDrawFunction](IMGUI.Controls.ArcHandle.DefaultAngleHandleDrawFunction.html)|
A CapFunction that draws a line terminated with Handles.CylinderHandleCap.  
---|---  
[DefaultAngleHandleSizeFunction](IMGUI.Controls.ArcHandle.DefaultAngleHandleSizeFunction.html)|
A SizeFunction that returns a fixed screen-space size.  
[DefaultRadiusHandleSizeFunction](IMGUI.Controls.ArcHandle.DefaultRadiusHandleSizeFunction.html)|
A SizeFunction that returns a fixed screen-space size.  
  
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

