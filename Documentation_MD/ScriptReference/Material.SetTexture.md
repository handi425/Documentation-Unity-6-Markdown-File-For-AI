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

#  [Material](Material.html).SetTexture

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

public void SetTexture(string name, [Texture](Texture.html) value);

## Declaration

public void SetTexture(int nameID, [Texture](Texture.html) value);

## Declaration

public void SetTexture(string name, [RenderTexture](RenderTexture.html) value,
[Rendering.RenderTextureSubElement](Rendering.RenderTextureSubElement.html)
element);

## Declaration

public void SetTexture(int nameID, [RenderTexture](RenderTexture.html) value,
[Rendering.RenderTextureSubElement](Rendering.RenderTextureSubElement.html)
element);

### Parameters

nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
---|---  
name | Property name, e.g. "_MainTex".  
value | Texture to set.  
element | Optional parameter that specifies the type of data to set from the RenderTexture.  
  
### Description

Sets a named texture.

Many shaders use more than one texture. Use SetTexture to change the texture
(identified by shader property name, or unique property name ID).  
  
When setting textures on materials using the Standard Shader, you should be
aware that you may need to use [EnableKeyword](Material.EnableKeyword.html) to
enable features of the shader that were not previously in use. For more
detail, read [Accessing Materials via
Script](../Manual/MaterialsAccessingViaScript.html).  
  
Common texture names used by Unity's builtin shaders:  
`"_MainTex"` is the main diffuse texture. This can also be accessed via
[mainTexture](Material-mainTexture.html) property.  
`"_BumpMap"` is the normal map.  
  
The shader properties also show some of the keywords needed to set the Texture
of a Material. To see this, go to your Material and right click on the
**Shader** dropdown at the top. Next, pick **Select Shader**.  
  
By specifying a `RenderTextureSubElement`, you can indicate which type of data
to set from the RenderTexture. The possible options are:
[RenderTextureSubElement.Color](Rendering.RenderTextureSubElement.Color.html),
[RenderTextureSubElement.Depth](Rendering.RenderTextureSubElement.Depth.html),
and
[RenderTextureSubElement.Stencil](Rendering.RenderTextureSubElement.Stencil.html).  
  
Additional resources: [mainTexture](Material-mainTexture.html) property,
[GetTexture](Material.GetTexture.html),
[Shader.PropertyToID](Shader.PropertyToID.html), [Properties in Shader
Programs](../Manual/SL-PropertiesInPrograms.html),
[RenderTextureSubElement](Rendering.RenderTextureSubElement.html).

    
    
    //Attach this script to your [GameObject](GameObject.html) (make sure it has a [Renderer](Renderer.html) component)
    //Click on the [GameObject](GameObject.html). Attach your own Textures in the [GameObject](GameObject.html)’s Inspector.  
      
    //This script takes your [GameObject](GameObject.html)’s material and changes its Normal Map, Albedo, and Metallic properties to the Textures you attach in the [GameObject](GameObject.html)’s Inspector. This happens when you enter Play [Mode](Scripting.GarbageCollector.Mode.html)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html) {  
      
        //Set these Textures in the Inspector
        public [Texture](Texture.html) m_MainTexture, m_Normal, m_Metal;
        [Renderer](Renderer.html) m_Renderer;  
      
        // Use this for initialization
        void Start () {
            //Fetch the [Renderer](Renderer.html) from the [GameObject](GameObject.html)
            m_Renderer = GetComponent<[Renderer](Renderer.html)> ();  
      
            //Make sure to enable the Keywords
            m_Renderer.material.EnableKeyword ("_NORMALMAP");
            m_Renderer.material.EnableKeyword ("_METALLICGLOSSMAP");  
      
            //Set the [Texture](Texture.html) you assign in the Inspector as the main texture (Or Albedo)
            m_Renderer.material.SetTexture("_MainTex", m_MainTexture);
            //Set the Normal map using the [Texture](Texture.html) you assign in the Inspector
            m_Renderer.material.SetTexture("_BumpMap", m_Normal);
            //Set the Metallic [Texture](Texture.html) as a [Texture](Texture.html) you assign in the Inspector
            m_Renderer.material.SetTexture ("_MetallicGlossMap", m_Metal);
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

