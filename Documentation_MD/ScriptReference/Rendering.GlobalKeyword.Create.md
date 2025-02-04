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

#  [GlobalKeyword](Rendering.GlobalKeyword.html).Create

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

public static [Rendering.GlobalKeyword](Rendering.GlobalKeyword.html)
Create(string name);

### Parameters

name | The name of the global shader keyword.  
---|---  
  
### Returns

**GlobalKeyword** Returns a new instance of the GlobalKeyword class.

### Description

Creates and returns a [GlobalKeyword](Rendering.GlobalKeyword.html) that
represents a new or existing global shader keyword.

Unity creates and returns a `GlobalKeyword` struct to represent the global
shader keyword with the given name. If a global shader keyword with the given
name does not yet exist in Unity's internal list of global shader keywords,
Unity adds a global shader keyword with the given name to the list.  
  
The following example creates a `GlobalKeyword` struct with the name
`EXAMPLE_FEATURE_ON`, and caches it. It provides functions to enable and
disable it.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class GlobalKeywordExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GlobalKeyword](Rendering.GlobalKeyword.html) exampleFeatureKeyword;  
      
        private void Start()
        {
            exampleFeatureKeyword = [GlobalKeyword.Create](Rendering.GlobalKeyword.Create.html)("EXAMPLE_FEATURE_ON");
        }  
      
        public void EnableExampleFeature()
        {
            [Shader.EnableKeyword](Shader.EnableKeyword.html)(exampleFeatureKeyword);
        }  
      
        public void DisableExampleFeature()
        {
            [Shader.DisableKeyword](Shader.DisableKeyword.html)(exampleFeatureKeyword);
        }
    }
    

Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[EnableKeyword](Shader.EnableKeyword.html),
[DisableKeyword](Shader.DisableKeyword.html),
[SetKeyword](Shader.SetKeyword.html),
[IsKeywordEnabled](Shader.IsKeywordEnabled.html),
[enabledGlobalKeywords](Shader-enabledGlobalKeywords.html),
[globalKeywords](Shader-globalKeywords.html).

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

