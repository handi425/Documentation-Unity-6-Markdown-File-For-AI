[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/srp-setting-render-pipeline-asset.html)
  * [中文](/cn/current/Manual/srp-setting-render-pipeline-asset.html)
  * [日本語](/ja/current/Manual/srp-setting-render-pipeline-asset.html)
  * [한국어](/kr/current/Manual/srp-setting-render-pipeline-asset.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/srp-setting-render-pipeline-asset.html)
  * [中文](/cn/current/Manual/srp-setting-render-pipeline-asset.html)
  * [日本語](/ja/current/Manual/srp-setting-render-pipeline-asset.html)
  * [한국어](/kr/current/Manual/srp-setting-render-pipeline-asset.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Choosing a render pipeline](choose-a-render-pipeline-landing.html)
  * Change or detect the active render pipeline

[](render-pipelines-set-up.html)

Set up a render pipeline

[](rendering-paths-introduction.html)

Rendering paths in Unity

# Change or detect the active render pipeline

This page contains information on how to get, set, and configure the **render
pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) that Unity is currently using.
The render pipeline that Unity is currently using is called the active render
pipeline.

## Overview

To render content, Unity can either use the Built-in Render Pipeline or a
render pipeline based on the [Scriptable Render Pipeline](scriptable-render-
pipeline-introduction.html) (SRP), which includes the Universal Render
Pipeline (URP) and the High Definition Render Pipeline (HDRP).

To specify which Scriptable Render Pipeline Unity uses, you use Render
Pipeline Assets. A Render Pipeline Asset tells Unity which SRP to use, and how
to configure it. If you don’t specify a Render Pipeline Asset, Unity uses the
Built-in Render Pipeline.

You can create multiple Render Pipeline Assets that use the same render
pipeline, but with different configurations; for example, you can use
different Render Pipeline Assets for different hardware quality levels. For a
general introduction to Render Pipeline Assets, see [Scriptable Render
Pipeline introduction](scriptable-render-pipeline-introduction.html). For
information on URP’s Render Pipeline Asset, see [The Universal Render Pipeline
Asset](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/manual/universalrp-
asset.html), and for HDRP’s Render Pipeline Asset, see [The High Definition
Render Pipeline Asset](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.high-definition@latest/index.html?subfolder=/manual/HDRP-
Asset.html).

As soon as you change the active render pipeline in the Unity Editor or at
runtime, Unity uses the new active render pipeline to render content. If you
are in the Unity Editor, this includes the Game view, the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view, and previews for Materials in the
Project panel and the **Inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

When you change the active render pipeline, you must ensure that the assets
and code in your project are compatible with the new render pipeline;
otherwise, you might experience errors or unintended visual effects.

## Determining the active render pipeline

Settings in both [Graphics Settings](class-GraphicsSettings.html) and [Quality
Settings](class-QualitySettings.html) determine the active render pipeline. In
Graphics Settings, you configure the render pipeline that Unity uses by
default. In Quality Settings, you can override the default render pipeline for
a given quality level.

To get or set the default render pipeline, use Graphics Settings >
**Scriptable Render Pipeline Setting** (or its equivalent API,
[GraphicsSettings.defaultRenderPipeline](../ScriptReference/Rendering.GraphicsSettings-
defaultRenderPipeline.html)). To get or set the render pipeline that overrides
the default for a given quality level, Quality Settings > **Render Pipeline**
(or its equivalent API,
[QualitySettings.renderPipeline](../ScriptReference/QualitySettings-
renderPipeline.html)).

Unity determines the active render pipeline like this:

  * If the current Quality Settings level > **Render Pipeline** references a Render Pipeline Asset, Unity uses that value.
  * Otherwise: 
    * If Graphics Settings > **Scriptable Render Pipeline Setting** references a Render Pipeline Asset, Unity uses that value.
    * Otherwise, Unity uses the Built-in Render Pipeline.

## How to get and set the active render pipeline in the Editor UI

### Getting the active render pipeline

To get the active render pipeline in the Editor **UI**(User Interface) Allows
a user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), you must check both the Graphics Settings
and Quality Settings windows. For information on how to use these values to
determine the active render pipeline, see Determining the active render
pipeline.

### Activating the Built-in Render Pipeline

To set the active render pipeline to the Built-in Render Pipeline, remove any
Render Pipeline Assets from Graphics Settings and Quality Settings.

To do this:

  1. Select **Edit** > **Project Settings** > **Quality**.
  2. For each quality level, if a Render Pipeline Asset is assigned to the **Render Pipeline** field, unassign it.
  3. Select **Edit** > **Project Settings** > **Graphics**.
  4. If a Render Pipeline Asset is assigned to the **Scriptable Render Pipeline Setting** field, unassign it.

### Activating URP, HDRP, or a custom render pipeline based on SRP

To set the active render pipeline to one that is based on SRP, tell Unity
which Render Pipeline Asset to use as the default active render pipeline, and
optionally which Render Pipeline Assets to use for each quality level.

To do this:

  1. In your Project folder, locate the Render Pipeline Asset(s) that you want to use.
  2. Set the default render pipeline, which Unity uses when there is no override for a given quality level. If you do not set this, Unity uses the Built-in Render Pipeline when no override applies. 
    1. Select **Edit** > **Project Settings** > **Graphics**.
    2. Drag the Render Pipeline Asset on to the **Scriptable Render Pipeline Setting** field.
  3. **Optional** : Set override Render Pipeline Assets for different quality levels. 
    1. Select **Edit** > **Project Settings** > **Quality**.
    2. Drag the Render Pipeline Asset on to the **Render Pipeline** field.

## How to get and set the active render pipeline in C# scripts

In C# **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), you can get and set the active
render pipeline and receive a callback when the active render pipeline
changes. You can do this in Edit Mode or Play Mode in the Unity Editor, or at
runtime in your application.

To do this, use the following APIs:

  * There are several ways to get the active render pipeline: 
    * To get a reference to the Render Pipeline Asset that defines the active render pipeline, use [GraphicsSettings.currentRenderPipeline](../ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html).
    * To get a reference to the Render Pipeline Asset that defines the active render pipeline and to determine whether Unity is using the default value or an override value, get the values of [GraphicsSettings.defaultRenderPipeline](../ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) and [QualitySettings.renderPipeline](../ScriptReference/QualitySettings-renderPipeline.html). For information on how to use these values, see Determining the active render pipeline or the following code sample.
    * To get the [RenderPipeline](../ScriptReference/Rendering.RenderPipeline.html) instance for the active render pipeline, use [RenderPipelineManager.currentPipeline](../ScriptReference/Rendering.RenderPipelineManager-currentPipeline.html). **Note:** Unity updates this property only after it has rendered at least one frame with the active render pipeline.
  * To set the active render pipeline, set the values of [GraphicsSettings.defaultRenderPipeline](../ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) and [QualitySettings.renderPipeline](../ScriptReference/QualitySettings-renderPipeline.html). For information on how to use these values, see Determining the active render pipeline or the following code sample.
  * To detect and execute code when the type of the active render pipeline changes, use [RenderPipelineManager.activeRenderPipelineTypeChanged](../ScriptReference/Rendering.RenderPipelineManager-activeRenderPipelineTypeChanged.html).

The following example code shows how to use these APIs:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
     
    public class ActiveRenderPipelineExample : MonoBehaviour
    {
        // In the Inspector, assign a Render Pipeline Asset to each of these fields
        public RenderPipelineAsset defaultRenderPipelineAsset;
        public RenderPipelineAsset overrideRenderPipelineAsset;
     
        void Start()
        {
            GraphicsSettings.defaultRenderPipeline = defaultRenderPipelineAsset;
            QualitySettings.renderPipeline = overrideRenderPipelineAsset;
    
            DisplayCurrentRenderPipeline();
        }
    
        void Update()
        {
            // When the user presses the left shift key, switch the default render pipeline
            if (Input.GetKeyDown(KeyCode.LeftShift)) {
                SwitchDefaultRenderPipeline();
                DisplayCurrentRenderPipeline();
            }
            // When the user presses the right shift key, switch the override render pipeline
            else if (Input.GetKeyDown(KeyCode.RightShift)) {
                SwitchOverrideRenderPipeline();
                DisplayCurrentRenderPipeline();
            }
        }
    
        // Switch the default render pipeline between null,
        // and the render pipeline defined in defaultRenderPipelineAsset
        void SwitchDefaultRenderPipeline()
        {
            if (GraphicsSettings.defaultRenderPipeline == defaultRenderPipelineAsset)
            {
                GraphicsSettings.defaultRenderPipeline = null;
            }
            else
            {
                GraphicsSettings.defaultRenderPipeline = defaultRenderPipelineAsset;
            }
        }
    
        // Switch the override render pipeline between null,
        // and the render pipeline defined in overrideRenderPipelineAsset
        void SwitchOverrideRenderPipeline()
        {
            if (QualitySettings.renderPipeline == overrideRenderPipelineAsset)
            {
                QualitySettings.renderPipeline = null;
            }
            else
            {
               QualitySettings.renderPipeline = overrideRenderPipelineAsset;
            }
        }
    
        // Print the current render pipeline information to the console
        void DisplayCurrentRenderPipeline()
        {
            // GraphicsSettings.defaultRenderPipeline determines the default render pipeline
            // If it is null, the default is the Built-in Render Pipeline
            if (GraphicsSettings.defaultRenderPipeline != null)
            {
                Debug.Log("The default render pipeline is defined by " + GraphicsSettings.defaultRenderPipeline.name);
            }
            else
            {
                Debug.Log("The default render pipeline is the Built-in Render Pipeline");
            }
    
            // QualitySettings.renderPipeline determines the override render pipeline for the current quality level
            // If it is null, no override exists for the current quality level
            if (QualitySettings.renderPipeline != null)
            {
                Debug.Log("The override render pipeline for the current quality level is defined by " + QualitySettings.renderPipeline.name);
            }
            else
            {
                Debug.Log("No override render pipeline exists for the current quality level");
            }
    
            // If an override render pipeline is defined, Unity uses that
            // Otherwise, it falls back to the default value
            if (QualitySettings.renderPipeline != null)
            {
                Debug.Log("The active render pipeline is the override render pipeline");
            }
            else
            {
                Debug.Log("The active render pipeline is the default render pipeline");
            }
    
            // To get a reference to the Render Pipeline Asset that defines the active render pipeline,
            // without knowing if it is the default or an override, use GraphicsSettings.currentRenderPipeline
            if (GraphicsSettings.currentRenderPipeline != null)
            {
                Debug.Log("The active render pipeline is defined by " +GraphicsSettings.currentRenderPipeline.name);
            }
            else
            {
                Debug.Log("The active render pipeline is the Built-in Render Pipeline");
            }
        }
    }
    

[](render-pipelines-set-up.html)

Set up a render pipeline

[](rendering-paths-introduction.html)

Rendering paths in Unity

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

