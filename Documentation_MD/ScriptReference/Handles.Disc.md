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

#  [Handles](Handles.html).Disc

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

public static [Quaternion](Quaternion.html) Disc(int id,
[Quaternion](Quaternion.html) rotation, [Vector3](Vector3.html) position,
[Vector3](Vector3.html) axis, float size, bool cutoffPlane, float snap);

## Declaration

public static [Quaternion](Quaternion.html) Disc([Quaternion](Quaternion.html)
rotation, [Vector3](Vector3.html) position, [Vector3](Vector3.html) axis,
float size, bool cutoffPlane, float snap);

### Parameters

id | The control ID of the handle.  
---|---  
rotation | The rotation of the disc.  
position | The center of the disc.  
axis | The axis to rotate around.  
size | The size of the disc in world space.  
cutoffPlane | If true, only the front-facing half of the circle is draw / draggable. This is useful when you have many overlapping rotation axes (like in the default rotate tool) to avoid clutter.  
snap | The grid size to snap to.  
  
### Returns

**Quaternion** The new rotation value modified by the user's interaction with
the handle. If the user has not moved the handle, it will return the same
value as you passed into the function.

### Description

Make a 3D disc that can be dragged with the mouse.

**Note:** Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)
where you might want to have constant screen-sized handles.  
  
![](../StaticFiles/ScriptRefImages/DiscHandle.png)  
_Disc Handle on the Scene View._

    
    
    // Name this script "DiscHandleEditor"
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(DiscHandle))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class DiscHandleEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            DiscHandle t = (target as DiscHandle);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Quaternion](Quaternion.html) rot = [Handles.Disc](Handles.Disc.html)(t.rot, t.transform.position, new [Vector3](Vector3.html)(1, 1, 0), 5, false, 1);  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Disc [Rotate](UIElements.Rotate.html)");
                t.rot = rot;
                t.Update();
            }
        }
    }
    

And the script attached to this Handle:

    
    
    // Name this script "DiscHandle"
    using UnityEngine;
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class DiscHandle : [MonoBehaviour](MonoBehaviour.html)
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

