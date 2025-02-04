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

#  [Material](Material.html).SetKeyword

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

## Declaration

public void SetKeyword(ref
[Rendering.LocalKeyword](Rendering.LocalKeyword.html) keyword, bool value);

### Parameters

keyword | The [LocalKeyword](Rendering.LocalKeyword.html) to enable or disable.  
---|---  
value | The desired keyword state.  
  
### Description

Sets the state of a local shader keyword for this material.

Shader keywords determine which shader variants Unity uses. For information on
working with [local shader keywords](Rendering.LocalKeyword.html) and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
When `value` is `true`, this function calls
[EnableKeyword](Material.EnableKeyword.html). Otherwise, it calls
[DisableKeyword](Material.DisableKeyword.html).  
  
If the [LocalKeyword](Rendering.LocalKeyword.html) does not exist in the
[Shader.keywordSpace](Shader-keywordSpace.html) for the shader that this
material uses, this function has no effect.  
  
The following example creates and caches a `LocalKeyword`, and provides a
function to toggle its state.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class MaterialKeywordExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) material;
        private [LocalKeyword](Rendering.LocalKeyword.html) exampleFeatureKeyword;  
      
        void Start()
        {
            // Get the instance of the [Shader](Shader.html) class that this material uses
            var shader = material.shader;  
      
            // Create and cache the [LocalKeyword](Rendering.LocalKeyword.html)
            exampleFeatureKeyword = new [LocalKeyword](Rendering.LocalKeyword.html)(shader, "EXAMPLE_FEATURE_ON");
        }  
      
        public void ToggleExampleFeature()
        {
            // Get the current state of the local keyword
            bool state = material.IsKeywordEnabled(exampleFeatureKeyword);  
      
            // [Toggle](UIElements.Toggle.html) the state
            material.SetKeyword(exampleFeatureKeyword, !state);
        }
    }
    

Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[EnableKeyword](Material.EnableKeyword.html),
[DisableKeyword](Material.DisableKeyword.html), [Shader.keywordSpace](Shader-
keywordSpace.html), [IsKeywordEnabled](Material.IsKeywordEnabled.html),
[enabledKeywords](Material-enabledKeywords.html), [shaderKeywords](Material-
shaderKeywords.html).

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

