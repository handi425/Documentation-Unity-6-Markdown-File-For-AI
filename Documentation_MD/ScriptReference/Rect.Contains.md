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

#  [Rect](Rect.html).Contains

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

public bool Contains([Vector2](Vector2.html) point);

## Declaration

public bool Contains([Vector3](Vector3.html) point);

## Declaration

public bool Contains([Vector3](Vector3.html) point, bool allowInverse);

### Parameters

point | Point to test.  
---|---  
allowInverse | Does the test allow the Rect's width and height to be negative?  
  
### Returns

**bool** True if the point lies within the specified rectangle.

### Description

Returns true if the `x` and `y` components of `point` is a point inside this
rectangle. If `allowInverse` is present and true, the width and height of the
Rect are allowed to take negative values (ie, the min value is greater than
the max), and the test will still work.

    
    
    using UnityEngine;  
      
    public class RectExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            [Rect](Rect.html) rect = new [Rect](Rect.html)(0, 0, 150, 150);
            if (rect.Contains([Input.mousePosition](Input-mousePosition.html)))
                [Debug.Log](Debug.Log.html)("Inside");
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

