[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/ShaderGraph.html)
  * [中文](/cn/current/Manual/urp/ShaderGraph.html)
  * [日本語](/ja/current/Manual/urp/ShaderGraph.html)
  * [한국어](/kr/current/Manual/urp/ShaderGraph.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/ShaderGraph.html)
  * [中文](/cn/current/Manual/urp/ShaderGraph.html)
  * [日本語](/ja/current/Manual/urp/ShaderGraph.html)
  * [한국어](/kr/current/Manual/urp/ShaderGraph.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * Create a 2D sprite lit Shader Graph in URP

[](../urp/2DShadows.html)

Create shadows with Shadow Caster 2D in URP

[](../urp/2d-visual-effect-graph-compatibility.html)

Light a VFX Graph asset with 2D lights in URP

# Create a 2D sprite lit Shader Graph in URP

Create a **shader** A program that runs on the GPU. [More
info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) that reacts to 2D lights when
applied to materials.

## Create a Sprite Lit Shader Graph

  1. Create a new asset by selecting **Assets > Create > Shader Graph > URP > Sprite Lit Shader Graph**. The Shader Graph asset is then created in the asset window.  
![](../../uploads/urp/2D/2d-urp12-create-lit-shader.png)

  2. Double-click the new asset to open the **Shader Graph**.  
![](../../uploads/urp/2D/2d-urp12-open-shader-graph.png)

  3. Create three **Sample Texture 2D** Nodes by right-clicking on the Shader Graph window and selecting **Create Node** , then search for and select the **Sample Texture 2D** option.  
![](../../uploads/urp/2D/2d-urp12-create-node.png)

  4. Change the **Type** of one of the Nodes to **Normal**.  
![](../../uploads/urp/2D/2d-urp12-3-node-normal.png)

  5. Attach the RGBA(4) **Output Slot** of the **Default Type** Nodes as shown below. Note that you should attach the **Normal Type** Node’s Output Slot to the **Normal(Tangent Space)(3)** Input Slot.  
![](../../uploads/urp/2D/2d-urp12-attach-textures.png)

  6. Create three **Texture 2D** properties by selecting the **+** on the [Blackboard](http://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Blackboard.html), and then select **Texture 2D**. Name them ‘MainTex’, ‘MaskTex’, and ‘NormalMap’ for this example.  
![](../../uploads/urp/2D/2d-urp12-3-create-texture-2D.png)
![](../../uploads/urp/2D/2d-urp12-3-three-textures.png)

  7. Drag each of the **Texture 2D** properties onto the editor window. Attach each of the properties to the **Input Slots** of the Sample Texture 2D Nodes as shown below. Note that the ‘NormalMap’ property must be attached to the **Normal Type** Node only.  
![](../../uploads/urp/2D/2d-urp12-3-attach-properties.png)

  8. Select **Save Asset** to save the Shader.  
![](../../uploads/urp/2D/2d-urp12-3-save-shader.png)

You can now apply the newly built Shader to materials.

[](../urp/2DShadows.html)

Create shadows with Shadow Caster 2D in URP

[](../urp/2d-visual-effect-graph-compatibility.html)

Light a VFX Graph asset with 2D lights in URP

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

