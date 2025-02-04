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

#  [Handles](Handles.html).Slider2D

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

## Declaration

public static [Vector3](Vector3.html) Slider2D(int id, [Vector3](Vector3.html)
handlePos, [Vector3](Vector3.html) offset, [Vector3](Vector3.html) handleDir,
[Vector3](Vector3.html) slideDir1, [Vector3](Vector3.html) slideDir2, float
handleSize, [Handles.CapFunction](Handles.CapFunction.html) capFunction,
[Vector2](Vector2.html) snap, bool drawHelper = false);

## Declaration

public static [Vector3](Vector3.html) Slider2D([Vector3](Vector3.html)
handlePos, [Vector3](Vector3.html) handleDir, [Vector3](Vector3.html)
slideDir1, [Vector3](Vector3.html) slideDir2, float handleSize,
[Handles.CapFunction](Handles.CapFunction.html) capFunction, float snap, bool
drawHelper = false);

## Declaration

public static [Vector3](Vector3.html) Slider2D(int id, [Vector3](Vector3.html)
handlePos, [Vector3](Vector3.html) handleDir, [Vector3](Vector3.html)
slideDir1, [Vector3](Vector3.html) slideDir2, float handleSize,
[Handles.CapFunction](Handles.CapFunction.html) capFunction,
[Vector2](Vector2.html) snap, bool drawHelper = false);

## Declaration

public static [Vector3](Vector3.html) Slider2D([Vector3](Vector3.html)
handlePos, [Vector3](Vector3.html) handleDir, [Vector3](Vector3.html)
slideDir1, [Vector3](Vector3.html) slideDir2, float handleSize,
[Handles.CapFunction](Handles.CapFunction.html) capFunction,
[Vector2](Vector2.html) snap, bool drawHelper = false);

### Parameters

id | (optional) override the default ControlID for this Slider2D instance.  
---|---  
handlePos | The position of the current point in the space of [Handles.matrix](Handles-matrix.html).  
offset | (optional) renders the Slider2D at handlePos, but treats the Slider2D's origin as handlePos + offset. Useful for Slider2D instances that are placed/rendered relative to another object or handle.  
handleDir | The direction of the handle in the space of [Handles.matrix](Handles-matrix.html), only used for rendering of the handle.  
slideDir1 | The first axis of the slider's plane of movement in the space of [Handles.matrix](Handles-matrix.html).  
slideDir2 | The second axis of the slider's plane of movement in the space of [Handles.matrix](Handles-matrix.html).  
handleSize | The size of the handle in the space of [Handles.matrix](Handles-matrix.html). Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | (float or Vector2) The snap increment along both axes, either uniform or per-axis. See [Handles.SnapValue](Handles.SnapValue.html).  
drawHelper | (default: false) render a rectangle around the handle when dragging.  
capFunction | The function to call for doing the actual drawing.  
  
### Returns

**Vector3** The new value modified by the user's interaction with the handle.
If the user has not moved the handle, it will return the position value passed
into the function.

### Description

Make a 3D slider that moves along a plane defined by two axes.

This method will draw a 3D-draggable handle on the screen. The handle is
constrained to sliding along a plane in 3D space.  
  
![](../StaticFiles/ScriptRefImages/SliderHandle2D.png)  
_2D slider handle in the Scene View._  
  
Add the following script to your Assets folder as Slider2DExample.cs and add
the Slider2DExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class Slider2DExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) targetPosition { get { return m_TargetPosition; } set { m_TargetPosition = value; } }
        [[SerializeField](SerializeField.html)]
        private [Vector3](Vector3.html) m_TargetPosition = new [Vector3](Vector3.html)(1f, 0f, 2f);  
      
        public virtual void [Update](PlayerLoop.Update.html)()
        {
            transform.LookAt(m_TargetPosition);
        }
    }
    

Add the following script to Assets/Editor as Slider2DExampleEditor.cs and
select the object with the Slider2DExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(Slider2DExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class Slider2DExampleEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            Slider2DExample example = (Slider2DExample)target;  
      
            float size = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)(example.targetPosition) * 0.5f;
            float snap = 0.1f;
            [Vector3](Vector3.html) handleDirection = [Vector3.up](Vector3-up.html);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Vector3](Vector3.html) newTargetPosition = [Handles.Slider2D](Handles.Slider2D.html)(example.targetPosition, handleDirection, [Vector3.right](Vector3-right.html), [Vector3.forward](Vector3-forward.html), size, [Handles.CircleHandleCap](Handles.CircleHandleCap.html), snap);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(example, "Change Look At [Target](GraphicsBuffer.Target.html) [Position](UIElements.Position.html)");
                example.targetPosition = newTargetPosition;
                example.Update();
            }
        }
    }
    

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

