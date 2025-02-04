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

#  [LocalKeyword](Rendering.LocalKeyword.html).isOverridable

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

public bool isOverridable;

### Description

Whether this local shader keyword can be overridden by a global shader
keyword. (Read Only).

When the state of a local shader keyword and a global shader keyword with the
same name contradict each other, Unity uses this value to determine whether
the keyword is enabled or disabled.

  * When `isOverridable` is `true`: If a [GlobalKeyword](Rendering.GlobalKeyword.html) with the same `name` exists and is enabled, Unity uses the state of the `GlobalKeyword`. Otherwise, Unity uses the state of the `LocalKeyword`.
  * When `isOverridable` is `false`: Unity always uses the state of the `LocalKeyword`.

To set the value of `isOverridable` to `true`, declare the shader keyword with
**global scope**. To set the value of `isOverridable` to `false`, declare the
shader keyword with **local scope**. For information on declaring shader
keywords with local or global scope, see [Shader keywords: Declaring keywords
with local or global scope](../Manual/shader-keywords#declaring-keywords-
scope.html).  
  
**Note:** If a keyword is declared with local or global scope in a
[Shader](Shader.html) source file, and a keyword with the same name is
declared in one of its dependencies, the scope in the source file overrides
the scope in the dependencies. Dependencies comprise all Shaders that are
included via the [Fallback command](../Manual/SL-Fallback.html), and Passes
that are included via the [UsePass command](../Manual/SL-UsePass.html).  
  
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
variants-and-keywords.html), [GlobalKeyword](Rendering.GlobalKeyword.html).

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

