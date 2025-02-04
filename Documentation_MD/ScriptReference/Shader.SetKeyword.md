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

#  [Shader](Shader.html).SetKeyword

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

[Switch to Manual](../Manual/class-Shader.html "Go to Shader Component in the
Manual")

## Declaration

public static void SetKeyword(ref
[Rendering.GlobalKeyword](Rendering.GlobalKeyword.html) keyword, bool value);

### Parameters

keyword | The [GlobalKeyword](Rendering.GlobalKeyword.html) to enable or disable.  
---|---  
value | The desired keyword state.  
  
### Description

Sets the state of a global shader keyword.

Shader keywords determine which shader variants Unity uses. For information on
working with [local shader keywords](Rendering.LocalKeyword.html) and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
When `value` is `true`, this function calls
[EnableKeyword](Shader.EnableKeyword.html). Otherwise, it calls
[DisableKeyword](Shader.DisableKeyword.html).  
  
The following example creates and caches a `GlobalKeyword`, and provides a
function to toggle its state.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class GlobalKeywordExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GlobalKeyword](Rendering.GlobalKeyword.html) exampleFeatureKeyword;  
      
        private void Start()
        {
            // Create and cache the [GlobalKeyword](Rendering.GlobalKeyword.html)
            exampleFeatureKeyword = [GlobalKeyword.Create](Rendering.GlobalKeyword.Create.html)("EXAMPLE_FEATURE_ON");
        }  
      
        public void ToggleExampleFeature()
        {
            // Get the current state of the global keyword
            bool state = [Shader.IsKeywordEnabled](Shader.IsKeywordEnabled.html)(exampleFeatureKeyword);  
      
            // [Toggle](UIElements.Toggle.html) the state
            [Shader.SetKeyword](Shader.SetKeyword.html)(exampleFeatureKeyword, !state);
        }
    }
    

Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[EnableKeyword](Shader.EnableKeyword.html),
[DisableKeyword](Shader.DisableKeyword.html),
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

