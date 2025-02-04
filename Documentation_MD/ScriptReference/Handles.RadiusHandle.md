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

#  [Handles](Handles.html).RadiusHandle

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

public static float RadiusHandle([Quaternion](Quaternion.html) rotation,
[Vector3](Vector3.html) position, float radius, bool handlesOnly);

## Declaration

public static float RadiusHandle([Quaternion](Quaternion.html) rotation,
[Vector3](Vector3.html) position, float radius);

### Parameters

rotation | The orientation of the handle in 3D space.  
---|---  
position | The center of the handle in 3D space.  
radius | Radius to modify.  
handlesOnly | Whether to omit the circular outline of the radius and only draw the point handles.  
  
### Returns

**float** The new value modified by the user's interaction with the handle. If
the user has not moved the handle, it will return the same value as you passed
into the function.  
  
**Note:** Use HandleUtility.GetHandleSize where you might want to have
constant screen-sized handles.

### Description

Make a Scene view radius handle.

![](../StaticFiles/ScriptRefImages/RadiusHandle.png)  
_RadiusHandle on the Scene View._

    
    
    // Name this script "EffectRadiusEditor"
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomEditor](CustomEditor.html)(typeof(EffectRadius))]
    public class EffectRadiusEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            EffectRadius t = (target as EffectRadius);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            float areaOfEffect = [Handles.RadiusHandle](Handles.RadiusHandle.html)([Quaternion.identity](Quaternion-identity.html), t.transform.position, t.areaOfEffect);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Changed Area Of Effect");
                t.areaOfEffect = areaOfEffect;
            }
        }
    }
    

And the Script attached to this GameObject:

    
    
    // Name this script "EffectRadius"
    using UnityEngine;
    using System.Collections;  
      
    public class EffectRadius : [MonoBehaviour](MonoBehaviour.html)
    {
        public float areaOfEffect = 1;
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

