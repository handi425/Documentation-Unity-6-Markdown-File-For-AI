[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Setup.html)
  * [中文](/cn/current/Manual/urp/Setup.html)
  * [日本語](/ja/current/Manual/urp/Setup.html)
  * [한국어](/kr/current/Manual/urp/Setup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Setup.html)
  * [中文](/cn/current/Manual/urp/Setup.html)
  * [日本語](/ja/current/Manual/urp/Setup.html)
  * [한국어](/kr/current/Manual/urp/Setup.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * Set up the 2D Renderer asset in URP

[](../urp/2d-light-properties-explained.html)

Configure a 2D light

[](../urp/PrepShader.html)

Prepare and upgrade sprites for 2D lighting in URP

# Set up the 2D Renderer asset in URP

Install the following Editor and package versions to begin working with the
**2D Renderer** :

  * **Unity 2021.2.0b1** or later

  * **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline)** version 10 or higher
(available via the Package Manager)

  * Create a new Project using the [2D template](https://docs.unity3d.com/hub/manual/Templates.html#core-templates).  
![](../../uploads/urp/2D/New_Project_With_Template.png)

  * Create a new **Pipeline Asset** and **Renderer Asset** by going to the **Assets** menu and selecting **Create > Rendering > URP Asset (with 2D Renderer)**.  
![](../../uploads/urp/2D/2d-urp12-create-renderer-asset.png)

  * Enter the name for both the Pipeline and Renderer Assets. The name is automatically applied to both, with “_Renderer” appended to the name of the Renderer Asset.  
![](../../uploads/urp/2D/2d-urp12-pipeline-renderer-assets.png)

  * The Renderer Asset is automatically assigned to the Pipeline Asset.  
![](../../uploads/urp/2D/2d-urp12-pipeline-renderer-assigned.png)

  * To set the graphics quality settings, there are two options:

**Option 1: For a single setting across all platforms** 1\. Go to **Edit >
Project Settings** and select the **Graphics** category.  
![](../../uploads/urp/2D/2d-urp12-graphics-srpsettings.png)

  1. Drag the **Pipeline Asset** created earlier to the **Scriptable Render Pipeline Settings** box, and adjust the quality settings.

**Option 2: For settings per quality level** 1\. Go to **Edit > Project
Settings** and select the [Quality](https://docs.unity3d.com/Manual/class-
QualitySettings.html) category.  
![](../../uploads/urp/2D/2d-urp12-graphics-qualitysettings.png)

  1. Select the quality levels to be included in your Project.
  2. Drag the **Pipeline Asset** created earlier to the **Rendering** box.  
![](../../uploads/urp/2D/2d-urp12-graphics-quality-add-rendering-asset.png)

  3. Repeat steps 2–3 for each quality level and platform included in your Project.

The **2D Renderer** is now set up for your Project. **Note** : If you use the
**2D Renderer** in your Project, some of the options related to 3D rendering
in the **Universal Render Pipeline Asset** will not affect or impact on your
final app or game.

[](../urp/2d-light-properties-explained.html)

Configure a 2D light

[](../urp/PrepShader.html)

Prepare and upgrade sprites for 2D lighting in URP

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

