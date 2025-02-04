[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-get-started-with-text.html)
  * [中文](/cn/current/Manual/UIE-get-started-with-text.html)
  * [日本語](/ja/current/Manual/UIE-get-started-with-text.html)
  * [한국어](/kr/current/Manual/UIE-get-started-with-text.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-get-started-with-text.html)
  * [中文](/cn/current/Manual/UIE-get-started-with-text.html)
  * [日本語](/ja/current/Manual/UIE-get-started-with-text.html)
  * [한국어](/kr/current/Manual/UIE-get-started-with-text.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Get started with text 

[](UIE-work-with-text.html)

Work with text

[](UIB-styling-ui-text.html)

Style text with USS

# Get started with text

UI Toolkit uses TextCore to render text, a technology based on [TextMesh
Pro](https://docs.unity3d.com/Manual/com.unity.textmeshpro.html). TextCore
allows advanced styling capabilities and can render text clearly at various
point sizes and resolutions. It takes advantage of [Signed Distance Field
(SDF)](UIE-font-asset.html#sdf-fonts) font rendering, which can generate font
assets that look crisp even when transformed and magnified.

This example demonstrates how to style text in **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, create and apply static and
dynamic font assets, use rich text tags and custom style sheets to style text,
and create a UITK Text Settings asset to manage the text settings for a panel.

**Note** : For demonstration purposes, this guide uses a runtime UI. The
instructions to create font assets and a style sheet also apply to the Editor
UI. However, you can’t change the default UITK Text Settings for Editor UI in
the current release.

## Prerequisites

This guide is for developers familiar with the Unity Editor, UI Toolkit, and
C# scripting. Before you start, get familiar with the following:

  * [UI Builder](UIBuilder.html)
  * [UXML](UIE-UXML.html)
  * [Runtime UI](UIE-support-for-runtime-ui.html)

## Create a UITK Text Settings asset

Start with a runtime UI and create a [UITK Text Settings asset](UIE-text-
setting-asset.html) that manages text settings for the panel. You also create
a `Resources` folder and sub-folders to store font assets and custom style
sheets.

  1. Follow the steps in [Get started with Runtime UI](UIE-get-started-with-runtime-ui.html) to create a simple runtime UI.
  2. In the `Assets` folder, create a `Resources` folder.
  3. Right-click in the `Assets\UI Toolkit` folder, and select **Create** > **UI Toolkit** > **Text Settings** to create a `UITK Text Settings.asset`. The Inspector window for `UITK Text Settings.asset` shows the default path names for the font asset, Text Style Sheets asset, Sprite asset, and Color Gradient presets.
  4. In the `Resources` folder, create two folders named `Fonts & Materials` and `Text Style Sheets`.

## Style text with UI Builder

Use UI Builder to style the Toggle text to be bold and italic, and have a font
size of `12px`. For more information, see [Style text with USS](UIB-styling-
ui-text.html).

  1. Double-click `SimpleRuntimeUi.uxml` to open it in UI Builder.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window for the Toggle control,
select **Text**.

  3. In the **Font Style** field, select **B** and **I**.
  4. In the **Size** field, enter **12**.

## Create a static font asset

Create a [static font asset](UIE-font-asset.html#atlas-population-modes) and
apply it to the Button control. For a static font asset, you don’t need to
include the source font file in the build. However, you must generate atlas
for all the characters in the Button’s display text. The display text is `This
is a Button` and you will add a `*` in the text, so you generate atlas for
`TBhinostua*`.

  1. Download the [Lato](https://fonts.google.com/download?family=Lato) font package from Google Fonts.

  2. Unzip the font package file and place `Lato-Regula.ttf` in your project’s `Assets` folder.

  3. In the Inspector window for the font file, confirm the following: 

     * **Include Font Data** is enabled.
     * **Character** is set to **Dynamic**.
  4. In the Project window, right-click `Lato-Regula.ttf` and select **Create** > **Text Core** > **Font Asset** > **SDF**. This creates a dynamic font asset called `Lato-Regula SDF.asset`.

  5. In the Inspector window for `Lato-Regula SDF.asset`, set the **Atlas Population Mode** to **Static**.

  6. Click **Update Atlas Texture**.

  7. In the **Font Asset Creator** window, from the **Character Set** list, choose [**Custom Characters**](UIE-font-creator-properties.html#custom-characters). 

  8. In the **Custom Characters List** box, enter `TBhinostua*`.

  9. Click **Generate Font Atlas**.

  10. Save your changes.

  11. Place `Lato-Regula SDF.asset` in the `Assets\Resources\Fonts & Materials` folder.

  12. Double-click `SimpleRuntimeUi.uxml` to open it in UI Builder.

  13. In the Inspector window for the Button control, select **Text** > **Font Asset** > **Lato-Regula SDF**.

## Create a dynamic font asset

Create a [dynamic font asset](UIE-font-asset.html#atlas-population-modes) and
apply it to the **TextField control** A TextField control displays a non-
interactive piece of text to the user, such as a caption, label for other GUI
controls, or instruction. [More info](gui-Controls.html)  
See in [Glossary](Glossary.html#TextFieldcontrol). For a dynamic font asset,
you must include the source font file in the build. Import the source font
file directly to the path set for the font.

  1. Download the [Roboto](https://fonts.google.com/download?family=Roboto) font package from Google Fonts.

  2. Unzip the font package file and place `Roboto-Regular.ttf` in your project’s `Assets\Resources\Fonts & Materials` folder.

  3. In the Inspector window for the font file, confirm the following:

     * **Include Font Data** is enabled
     * **Character** is set to **Dynamic**
  4. Right-click `Roboto-Regular.ttf` and select **Create** > **Text Core** > **Font Asset**. This creates a dynamic font asset called `Roboto-Regular SDF.asset`.

  5. Double-click `SimpleRuntimeUi.uxml` to open it in UI Builder.

  6. In the TextField control’s Inspector window, select **Text** > **Font Asset** > **Roboto-Regular SDF**. 

## Style with rich text tags

Use [rich text tags](UIE-rich-text-tags.html) to style text in the Label
control.

**Note** : In the current release, rich text tags aren’t supported for
[TextField](UIE-uxml-element-TextField.html).

  1. Double-click `SimpleRuntimeUi.uxml` to open it in UI Builder.
  2. In the **Inspector** panel for the Label control, change **Text** to `This is a <font-weight=700><size=2em><color=#FF0000>*Label*</color></size></font-weight>`. This makes the word `Label` big, red, bold, and with an asterisk on either side of it.
  3. Make sure **Enable Rich Text** is selected.

The label text looks like the following in the **Viewport** The user’s visible
area of an app on their screen.  
See in [Glossary](Glossary.html#Viewport) window:

![Label text preview shows the word Label as big, red, and with an asterisk to
either side.](../uploads/Main/font/label-rich-text.png) Label text preview
shows the word “Label” as big, red, and with an asterisk to either side.

## Style with style sheets

To apply the same style for `Label` to `Button`, create a [custom style
sheet](UIE-style-sheet.html), and apply the style to both words.

  1. Right-click in the `Assets\Resources\Text Style Sheets` folder and select **Create** > **Text Core** > **Text StyleSheet**. This creates a `Text StyleSheet.asset` in the path you set in the UITK Text Settings asset.

  2. In the Inspector window for `Text StyleSheet.asset`, do the following:

     * In **Name** , enter `ExampleStyle`.
     * In **Opening Tags** , enter `<font-weight=700><size=2em><color=#FF0000>*`.
     * In **Closing Tags** , enter `*</color></size></font-weight>`.
  3. In the Inspector window for `UITK Text Settings.asset`, from the **Default Style Sheet** list, select **Text StyleSheet**.

  4. Double-click `SimpleRuntimeUi.uxml` to open it in UI Builder.

  5. In the Label control’s Inspector window, change **Text** to `<s>This is a <style="ExampleStyle">Label</style>`. 

  6. Make sure **Enable Rich Text** is selected.

  7. In the Button control’s Inspector window, change **Text** to `<s>This is a <style="ExampleStyle">Button</style>`.

  8. Make sure **Enable Rich Text** is selected.

  9. Enter Play mode and check the text in the runtime UI.

  10. In the text field, enter some random characters. For a dynamic font asset, the font atlas is dynamically generated as you enter text in the text field. 

  11. In your project’s `Assets\Resources\Fonts & Materials` folder, select `Roboto-Regular SDF.asset`.

  12. In the Inspector window for `Roboto-Regular SDF.asset`, select **Update Atlas Texture** to open the **Font Asset Creator** window. If the atlas window is hidden, expend it. You should see the characters you entered in the atlas window.

![Newly entered characters appear in the font atlas
window.](../uploads/Main/font/get-started-with-text.png) Newly entered
characters appear in the font atlas window.

## Additional resources

  * [Font Asset properties](UIE-font-asset-properties.html)
  * [Include sprites in text](UIE-sprite.html)
  * [Color gradients](UIE-color-gradient.html)
  * [Fallback font](UIE-fallback-font.html)
  * [Get started with runtime UI](UIE-get-started-with-runtime-ui.html)

[](UIE-work-with-text.html)

Work with text

[](UIB-styling-ui-text.html)

Style text with USS

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

