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

#  [Material](Material.html).SetTextureOffset

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

public void SetTextureOffset(string name, [Vector2](Vector2.html) value);

## Declaration

public void SetTextureOffset(int nameID, [Vector2](Vector2.html) value);

### Parameters

nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
---|---  
name | The name of the texture property as defined in the shader. For example: "_MainTex".  
value | Texture placement offset.  
  
### Description

Sets the placement offset of a given texture. The `name` parameter is defined
in the shader. This method creates a new Material instance.

Additional resources: [mainTextureOffset](Material-mainTextureOffset.html)
property, [GetTextureOffset](Material.GetTextureOffset.html),
[SetTexture](Material.SetTexture.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Scroll main texture based on time  
      
        float scrollSpeed = 0.5f;
        [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)> ();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float offset = [Time.time](Time-time.html) * scrollSpeed;
            rend.material.SetTextureOffset("_TextureName", new [Vector2](Vector2.html)(offset, 0));
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

