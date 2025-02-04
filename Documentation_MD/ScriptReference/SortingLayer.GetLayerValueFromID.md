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

#  [SortingLayer](SortingLayer.html).GetLayerValueFromID

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

public static int GetLayerValueFromID(int id);

### Parameters

id | The unique value of the sorting layer as returned by any renderer's sortingLayerID property.  
---|---  
  
### Returns

**int** The final sorting value of the layer relative to other layers.

### Description

Returns the final sorting layer value. To determine the sorting order between
the various sorting layers, use this method to retrieve the final sorting
value and use CompareTo to determine the order.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        int CompareLayer([GameObject](GameObject.html) rhs, [GameObject](GameObject.html) lhs)
        {
            int rval = [SortingLayer.GetLayerValueFromID](SortingLayer.GetLayerValueFromID.html)(rhs.GetComponent<[SpriteRenderer](SpriteRenderer.html)>().sortingLayerID);
            int lval = [SortingLayer.GetLayerValueFromID](SortingLayer.GetLayerValueFromID.html)(lhs.GetComponent<[SpriteRenderer](SpriteRenderer.html)>().sortingLayerID);
            return rval.CompareTo(lval);
        }
    }
    

Additional resources:
[GetLayerValueFromName](SortingLayer.GetLayerValueFromName.html).

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

