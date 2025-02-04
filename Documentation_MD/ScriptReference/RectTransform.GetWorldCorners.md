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

#  [RectTransform](RectTransform.html).GetWorldCorners

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

public void GetWorldCorners(Vector3[] fourCornersArray);

### Parameters

fourCornersArray | The array that corners are filled into.  
---|---  
  
### Description

Get the corners of the calculated rectangle in world space.

Each corner provides its world space value. The returned array of 4 vertices
is clockwise. It starts bottom left and rotates to top left, then top right,
and finally bottom right. Note that bottom left, for example, is an (x, y, z)
vector with x being left and y being bottom.  
  
**Note** : If the [RectTransform](RectTransform.html) is rotated in Z then the
dimensions of the [GetWorldCorners](RectTransform.GetWorldCorners.html) will
be changed.

    
    
    using UnityEngine;  
      
    // GetWorldCorners():
    //  Access the [RectTransform](RectTransform.html) and read the vertices
    //  that define the location and size of the
    //  object.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [RectTransform](RectTransform.html) rt;  
      
        void Start()
        {
            rt = GetComponent<[RectTransform](RectTransform.html)>();
            DisplayWorldCorners();
        }  
      
        void DisplayWorldCorners()
        {
            [Vector3](Vector3.html)[] v = new [Vector3](Vector3.html)[4];
            rt.GetWorldCorners(v);  
      
            [Debug.Log](Debug.Log.html)("World Corners");
            for (var i = 0; i < 4; i++)
            {
                [Debug.Log](Debug.Log.html)("World Corner " + i + " : " + v[i]);
            }
        }
    }
    

Additional resources: [GetLocalCorners](RectTransform.GetLocalCorners.html).

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

