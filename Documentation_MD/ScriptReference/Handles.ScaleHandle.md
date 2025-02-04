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

#  [Handles](Handles.html).ScaleHandle

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

public static [Vector3](Vector3.html) ScaleHandle([Vector3](Vector3.html)
scale, [Vector3](Vector3.html) position, [Quaternion](Quaternion.html)
rotation, float size);

### Parameters

scale | Scale to modify.  
---|---  
position | The position of the handle.  
rotation | The rotation of the handle.  
size | Allows you to scale the size of the handle on-screen.  
  
### Returns

**Vector3** The new value modified by the user's interaction with the handle.
If the user has not moved the handle, it will return the same value as you
passed into the function.

### Description

Make a Scene view scale handle.

This will behave like the built-in scale tool  
  
**Note:** Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)
where you might want to have constant screen-sized handles.  
  
![](../StaticFiles/ScriptRefImages/ScaleHandle.png)  
_Scale handle that will appear whenever you select the GameObject._

    
    
    // Name this script "ScaleAtPointEditor"
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(ScaleAtPoint))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class ScaleAtPointEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            ScaleAtPoint t = (target as ScaleAtPoint);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Vector3](Vector3.html) scale = [Handles.ScaleHandle](Handles.ScaleHandle.html)(t.scale, [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html), 1);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Scaled ScaleAt Point");
                t.scale = scale;
                t.Update();
            }
        }
    }
    

And the script Attached to this GameObject:

    
    
    // Name this script "ScaleAtPoint"
    using UnityEngine;
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ScaleAtPoint : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) scale = [Vector3.one](Vector3-one.html);
        public void [Update](PlayerLoop.Update.html)()
        {
            transform.localScale = scale;
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

