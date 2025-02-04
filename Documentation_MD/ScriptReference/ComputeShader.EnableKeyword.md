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

#  [ComputeShader](ComputeShader.html).EnableKeyword

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public void EnableKeyword(ref
[Rendering.LocalKeyword](Rendering.LocalKeyword.html) keyword);

## Declaration

public void EnableKeyword(string keyword);

### Parameters

keyword | The [LocalKeyword](Rendering.LocalKeyword.html) to enable.  
---|---  
keyword | The name of the [LocalKeyword](Rendering.LocalKeyword.html) to enable.  
  
### Description

Enables a local shader keyword for this compute shader.

Shader keywords determine which shader variants Unity uses. For information on
working with [local shader keywords](Rendering.LocalKeyword.html) and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
If you pass in a [LocalKeyword](Rendering.LocalKeyword.html) and it does not
exist in the [keywordSpace](ComputeShader-keywordSpace.html), this function
has no effect. If you pass a string and a
[LocalKeyword](Rendering.LocalKeyword.html) with that `name` does not exist in
the [keywordSpace](ComputeShader-keywordSpace.html), this function has no
effect.  
  
The version of this function that takes a string as a parameter is slower than
the version that takes a [LocalKeyword](Rendering.LocalKeyword.html). If you
call this function more than once, it is best practice to create a
[LocalKeyword](Rendering.LocalKeyword.html) struct, cache it, and use that.  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](Shader.html) or
[ComputeShader](ComputeShader.html) instance. You cannot use it with other
[Shader](Shader.html) or [ComputeShader](ComputeShader.html) instances, even
if they declare keywords with the same name.  
  
The following example creates a `LocalKeyword` struct with the name
`EXAMPLE_FEATURE_ON`, and caches it. It provides functions to enable and
disable it.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ComputeKeywordExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ComputeShader](ComputeShader.html) computeShader;
        private [LocalKeyword](Rendering.LocalKeyword.html) exampleFeatureKeyword;  
      
        void Start()
        {
            // Create and cache the [LocalKeyword](Rendering.LocalKeyword.html)
            exampleFeatureKeyword = new [LocalKeyword](Rendering.LocalKeyword.html)(computeShader, "EXAMPLE_FEATURE_ON");
        }  
      
        public void EnableExampleFeature()
        {
            computeShader.EnableKeyword(exampleFeatureKeyword);
        }  
      
        public void DisableExampleFeature()
        {
            computeShader.DisableKeyword(exampleFeatureKeyword);
        }
    }
    

Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[DisableKeyword](ComputeShader.DisableKeyword.html),
[SetKeyword](ComputeShader.SetKeyword.html), [keywordSpace](ComputeShader-
keywordSpace.html), [IsKeywordEnabled](ComputeShader.IsKeywordEnabled.html),
[enabledKeywords](ComputeShader-enabledKeywords.html),
[shaderKeywords](ComputeShader-shaderKeywords.html).

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

