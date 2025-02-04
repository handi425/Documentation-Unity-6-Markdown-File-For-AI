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

#  [Material](Material.html).IsKeywordEnabled

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

public bool IsKeywordEnabled(ref
[Rendering.LocalKeyword](Rendering.LocalKeyword.html) keyword);

## Declaration

public bool IsKeywordEnabled(string keyword);

### Parameters

keyword | The [LocalKeyword](Rendering.LocalKeyword.html) to check.  
---|---  
keyword | The name of the [LocalKeyword](Rendering.LocalKeyword.html) to check.  
  
### Returns

**bool** Returns `true` if a [LocalKeyword](Rendering.LocalKeyword.html) with
the given name is enabled for this material.

### Description

Checks whether a local shader keyword is enabled for this material.

Shader keywords determine which shader variants Unity uses. For information on
working with [local shader keywords](Rendering.LocalKeyword.html) and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
If you pass in a [LocalKeyword](Rendering.LocalKeyword.html) and it does not
exist in the [Shader.keywordSpace](Shader-keywordSpace.html) for the shader
that this material uses, this function returns `false`. If you pass a string
and a [LocalKeyword](Rendering.LocalKeyword.html) with that `name` does not
exist in the [Shader.keywordSpace](Shader-keywordSpace.html) for the shader
that this material uses, this function returns `false`.  
  
The version of this function that takes a string as a parameter is slower than
the version that takes a [LocalKeyword](Rendering.LocalKeyword.html). If you
call this function more than once, it is best practice to create a
[LocalKeyword](Rendering.LocalKeyword.html) struct, cache it, and use that.  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](Shader.html) or
[ComputeShader](ComputeShader.html) instance. You cannot use it with other
[Shader](Shader.html) or [ComputeShader](ComputeShader.html) instances, even
if they declare keywords with the same name.  
  
This example iterates over the local shader keywords in the local keyword
space for a material. It determines whether they are overridden by a global
shader keyword, and prints their state.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class KeywordExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) material;  
      
        void Start()
        {
            CheckShaderKeywordState();
        }  
      
        void CheckShaderKeywordState()
        {
            // Get the instance of the [Shader](Shader.html) class that the material uses
            var shader = material.shader;  
      
            // Get all the local keywords that affect the [Shader](Shader.html)
            var keywordSpace = shader.keywordSpace;  
      
            // Iterate over the local keywords
            foreach (var localKeyword in keywordSpace.keywords)
            {
                // If the local keyword is overridable,
                // and a global keyword with the same name exists and is enabled,
                // then Unity uses the global keyword state
                if (localKeyword.isOverridable && [Shader.IsKeywordEnabled](Shader.IsKeywordEnabled.html)(localKeyword.name))
                {
                    [Debug.Log](Debug.Log.html)("Local keyword with name of " + localKeyword.name + " is overridden by a global keyword, and is enabled");
                }
                // Otherwise, Unity uses the local keyword state
                else
                {
                    var state = material.IsKeywordEnabled(localKeyword) ? "enabled" : "disabled";
                    [Debug.Log](Debug.Log.html)("Local keyword with name of " + localKeyword.name + " is " + state);
                }
            }
        }
    }
    

Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[EnableKeyword](Material.EnableKeyword.html),
[DisableKeyword](Material.DisableKeyword.html),
[SetKeyword](Material.SetKeyword.html), [Shader.keywordSpace](Shader-
keywordSpace.html), [enabledKeywords](Material-enabledKeywords.html),
[shaderKeywords](Material-shaderKeywords.html).

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

