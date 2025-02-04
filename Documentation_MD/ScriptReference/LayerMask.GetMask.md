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

#  [LayerMask](LayerMask.html).GetMask

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

public static int GetMask(params string[] layerNames);

### Parameters

layerNames | List of layer names to convert to a layer mask.  
---|---  
  
### Returns

**int** The layer mask created from the `layerNames`.

### Description

Given a set of layer names as defined by either a Builtin or a User Layer in
the [Tags and Layers manager](../Manual/class-TagManager.html), returns the
equivalent layer mask for all of them.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)([LayerMask.GetMask](LayerMask.GetMask.html)("UserLayerA", "UserLayerB"));
        }
    }
    

**Note:** Suppose `UserLayerA` and `UserLayerB` are the tenth and eleventh
layers. These will have a User Layer values of 10 and 11. To obtain their
layer mask value their names can be passed into
[GetMask](LayerMask.GetMask.html). The argument can either be a list of their
names or an array of strings storing their names. In this case the return
value will be 2^10 + 2^11 = 3072.

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

