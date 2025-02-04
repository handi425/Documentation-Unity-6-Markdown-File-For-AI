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

#  [Handles](Handles.html).FreeMoveHandle

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

public static [Vector3](Vector3.html) FreeMoveHandle([Vector3](Vector3.html)
position, float size, [Vector3](Vector3.html) snap,
[Handles.CapFunction](Handles.CapFunction.html) capFunction);

## Declaration

public static [Vector3](Vector3.html) FreeMoveHandle(int controlID,
[Vector3](Vector3.html) position, float size, [Vector3](Vector3.html) snap,
[Handles.CapFunction](Handles.CapFunction.html) capFunction);

### Parameters

position | The position of the handle in the space of [Handles.matrix](Handles-matrix.html).  
---|---  
size | The size of the handle in the space of [Handles.matrix](Handles-matrix.html). Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment on all axes. See [Handles.SnapValue](Handles.SnapValue.html).  
capFunction | The function to call for doing the actual drawing.  
controlID | The control ID for the handle.  
  
### Returns

**Vector3** The new value modified by the user's interaction with the handle.
If the user has not moved the handle, it will return the same value as you
passed into the function.

### Description

Make an unconstrained movement handle.

This handle can move freely in all directions. Hold down Ctrl (Cmd on macOS)
to snap to the grid (see
[PositioningGameObjects](../Manual/PositioningGameObjects.html)). Hold Ctrl-
Shift (Cmd-Shift on macOS) to snap the object to any Collider surface under
the mouse pointer.  
  
![](../StaticFiles/ScriptRefImages/FreeMoveHandle.png)  
_Free Move handle in the Scene View._  
  
Add the following script to your Assets folder as FreeMoveHandleExample.cs and
add the FreeMoveHandleExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class FreeMoveHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) targetPosition { get { return m_TargetPosition; } set { m_TargetPosition = value; } }
        [[SerializeField](SerializeField.html)]
        private [Vector3](Vector3.html) m_TargetPosition = new [Vector3](Vector3.html)(1f, 0f, 2f);  
      
        public virtual void [Update](PlayerLoop.Update.html)()
        {
            transform.LookAt(m_TargetPosition);
        }
    }
    

Add the following script to Assets/Editor as FreeMoveHandleExampleEditor.cs
and select the object with the FreeMoveHandleExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(FreeMoveHandleExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class FreeMoveHandleExampleEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            FreeMoveHandleExample example = (FreeMoveHandleExample)target;  
      
            float size = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)(example.targetPosition) * 0.5f;
            [Vector3](Vector3.html) snap = [Vector3.one](Vector3-one.html) * 0.5f;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Vector3](Vector3.html) newTargetPosition = [Handles.FreeMoveHandle](Handles.FreeMoveHandle.html)(example.targetPosition, size, snap, [Handles.RectangleHandleCap](Handles.RectangleHandleCap.html));
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

