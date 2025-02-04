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

#  [Handles](Handles.html).FreeRotateHandle

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

public static [Quaternion](Quaternion.html) FreeRotateHandle(int id,
[Quaternion](Quaternion.html) rotation, [Vector3](Vector3.html) position,
float size);

## Declaration

public static [Quaternion](Quaternion.html)
FreeRotateHandle([Quaternion](Quaternion.html) rotation,
[Vector3](Vector3.html) position, float size);

### Parameters

id | The control ID of the handle.  
---|---  
rotation | The orientation of the handle in 3D space.  
position | The center of the handle in 3D space.  
size | The size of the handle.  
  
**Note:** Use HandleUtility.GetHandleSize where you might want to have
constant screen-sized handles.  
  
### Returns

**Quaternion** The new rotation value modified by the user's interaction with
the handle. If the user has not moved the handle, it will return the same
value as you passed into the function.

### Description

Make an unconstrained rotation handle.

The handle can rotate freely on all axes. The rotation gizmo has no visible
axes and is simply a circle in the Scene view. Users can click and drag from
within the circle to provide input rotation to your editor script.  
  
![](../StaticFiles/ScriptRefImages/FreeRotateHandle.png)  
_FreeRotate handle seen in the Scene View._

    
    
    // Name this script "FreeRotateEditor"
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(FreeRotate))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class FreeRotateEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            FreeRotate t = (target as FreeRotate);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Quaternion](Quaternion.html) rot = [Handles.FreeRotateHandle](Handles.FreeRotateHandle.html)(t.rot, [Vector3.zero](Vector3-zero.html), 2);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Free [Rotate](UIElements.Rotate.html)");
                t.rot = rot;
                t.Update();
            }
        }
    }
    

And the script attached to this Handle:

    
    
    // Name this script "FreeRotate"
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class FreeRotate : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Quaternion](Quaternion.html) rot = [Quaternion.identity](Quaternion-identity.html);
        public void [Update](PlayerLoop.Update.html)()
        {
            transform.rotation = rot;
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

