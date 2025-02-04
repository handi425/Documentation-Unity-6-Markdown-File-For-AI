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

#  [Material](Material.html).GetTag

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

public string GetTag(string tag, bool searchFallbacks);

## Declaration

public string GetTag(string tag, bool searchFallbacks, string defaultValue);

### Description

Get the value of material's shader tag.

If the material's shader does not define the tag, `defaultValue` is returned.  
  
If `searchFallbacks` is `true` then this function will look for tag in all
subshaders and all fallbacks. If `searchFallbacks` is `false` then only the
currently used subshader will be queried for the tag.  
  
Using `GetTag` without searching through fallbacks makes it possible to detect
which subshader is currently being used: add a custom tag to each subshader
with different value, and query the value at run time. For example, Unity
water uses this function to detect when the shader falls back to non-
reflective one, and turns off reflection camera in that case.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attach this to a gameObject that has a renderer.  
      
        string materialTag = "RenderType";  
      
        void Start()
        {
            [Renderer](Renderer.html) rend = GetComponent<[Renderer](Renderer.html)>();
            string result = rend.material.GetTag(materialTag, true, "Nothing");  
      
            if (result == "Nothing")
            {
                [Debug.LogError](Debug.LogError.html)(materialTag + " not found in " + rend.material.shader.name);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Tag found!, its value: " + result);
            }
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

