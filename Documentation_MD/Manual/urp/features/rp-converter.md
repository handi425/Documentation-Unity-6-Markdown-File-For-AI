[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/rp-converter.html)
  * [中文](/cn/current/Manual/urp/features/rp-converter.html)
  * [日本語](/ja/current/Manual/urp/features/rp-converter.html)
  * [한국어](/kr/current/Manual/urp/features/rp-converter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/rp-converter.html)
  * [中文](/cn/current/Manual/urp/features/rp-converter.html)
  * [日本語](/ja/current/Manual/urp/features/rp-converter.html)
  * [한국어](/kr/current/Manual/urp/features/rp-converter.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Installing and upgrading URP](../../urp/InstallingAndConfiguringURP.html)
  * [Upgrading from the Built-In Render Pipeline to URP](../../urp/upgrading-from-birp.html)
  * Convert assets using the Render Pipeline Converter

[](../../urp/upgrading-from-birp.html)

Upgrading from the Built-In Render Pipeline to URP

[](../../urp/upgrade-shaders-landing.html)

Upgrading shaders to URP from the Built-In Render Pipeline

# Convert assets using the Render Pipeline Converter

The ****Render Pipeline** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) Converter** converts
assets made for a Built-in Render Pipeline project to assets compatible with
URP.

> **Note** : The conversion process makes irreversible changes to the project.
> Back up your project before the conversion.

## How to use the Render Pipeline Converter

To convert project assets:

  1. Select **Window** > **Rendering** > **Render Pipeline Converter**. Unity opens the Render Pipeline Converter window.

![Render Pipeline Converter dialog](../../../uploads/urp/rp-converter/rp-
converter-dialog.png) Render Pipeline Converter dialog

  2. Select the conversion type.

![Conversion type](../../../uploads/urp/rp-converter/conversion-types.png)
Conversion type

  3. Depending on the conversion type, the dialog shows the available converters. Select or clear the check boxes next to converter names to enable or disable the converters.

![Select converters](../../../uploads/urp/rp-converter/select-converters.png)
Select converters

For the list of available converters, refer to the section Converters.

  4. Click **Initialize Converters**. The Render Pipeline Converter preprocesses the assets in the project and shows the list of elements to convert. Select or clear check boxes next to assets to include or exclude them from the conversion process.

![Initialize converters](../../../uploads/urp/rp-converter/initialize.png)
Initialize converters

The following illustration shows initialized converters.

![Initialized converters](../../../uploads/urp/rp-converter/after-
initialize.png) Initialized converters

Click a converter to check the list of items that a converter is about to
convert.

![Converter detailed view](../../../uploads/urp/rp-converter/converter-
detailed-view.png) Converter detailed view

**Yellow icon** : a yellow icon next to an element indicates that a user
action might be required to run the conversion. Hover the mouse pointer over
the icon to check the description of the issue.

  5. Click **Convert Assets** to start the conversion process.

> **Note** : The conversion process makes irreversible changes to the project.
> Back up your project before the conversion.

When the conversion process finishes, the window shows the status of each
converter.

![Conversion finished](../../../uploads/urp/rp-converter/conversion-
finished.png) Conversion finished

**Green check mark** : the conversion went without issues.

**Yellow icon** : the conversion finished with warnings and might require user
action.

**Red icon** : the conversion failed.

  6. Click a converter to check the list of processed items in that converter.

![Conversion finished. Detailed view of a converter](../../../uploads/urp/rp-
converter/conversion-finished-details.png) Conversion finished. Detailed view
of a converter

After reviewing the converted project, close the Render Pipeline Converter
window.

##  Conversion types and converters

The Render Pipeline Converter let’s you select one of the following conversion
types:

  * Built-in Render Pipeline to URP

  * Built-in Render Pipeline 2D to URP 2D

  * Upgrade 2D URP Assets

When you select on of the conversion types, the tool shows you the available
converters.

The following sections describe the converters available for each conversion
type.

### Built-in Render Pipeline to URP

This conversion type converts project elements from the Built-in Render
Pipeline to URP.

Available converters:

  * **Rendering Settings**

This converter creates the URP Asset and Renderer assets. Then the converter
evaluates the settings in the Built-in Render Pipeline project and converts
them into equivalent properties in the URP assets.

  * **Material Upgrade**

This converter converts the Materials. The converter works on pre-built
Materials that are supplied by Unity, it does not support Materials with
custom **shaders** A program that runs on the GPU. [More
info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader).

  * ****Animation Clip** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](../../class-AnimationClip.html)  
See in [Glossary](../../Glossary.html#AnimationClip) Converter**

This converter converts the animation clips. It runs after the **Material
Upgrade** converter finishes.

> **Note** : This converter is available only if the project contains
> animations that affect the properties of Materials, or Post-processing Stack
> v2 properties.

  * **Read-only Material Converter**

This converter converts the pre-built read-only Materials, where the
**Material Upgrade** converter cannot replace the shader. This converter
indexes the project and creates a temporary `.index` file, which might take a
significant time.

Examples of read-only Materials: `Default-Diffuse`, `Default-Line`, `Dafault-
Terrain-Diffuse`, etc.

  * ****Post-Processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../../Glossary.html#post-processing) Stack v2 Converter**

This converter converts PPv2 Volumes, Profiles, and Layers to URP Volumes,
Profiles, and **Cameras** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera). This converter indexes the
project and creates a temporary `.index` file, which might take a significant
time.

### Built-in Render Pipeline 2D to URP 2D

This conversion type converts elements of a project from Built-in Render
Pipeline 2D to URP 2D.

Available converters:

  * **Material and Material Reference Upgrade**

This converter converts all Materials and Material references from Built-in
Render Pipeline 2D to URP 2D.

### Upgrade 2D URP Assets

This conversion type upgrades assets of a 2D project from an earlier URP
version to the current URP version.

Available converters:

  * **Parametric to Freeform Light Upgrade**

This converter converts all parametric lights to freeform lights.

# Run conversion using API or CLI

The Render Pipeline Converter implements the
[Converters](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEditor.Rendering.Universal.Converters.html)
class with
[RunInBatchMode](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEditor.Rendering.Universal.Converters.html#UnityEditor_Rendering_Universal_Converters_RunInBatchMode_UnityEditor_Rendering_Universal_ConverterContainerId_)
methods that let you run the conversion process from a command line.

For example, the following script initializes and executes the converters
**Material Upgrade** , and **Read-only Material Converter**.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEditor;
    using UnityEditor.Rendering.Universal;
    using UnityEngine;
    
    public class MyUpgradeScript : MonoBehaviour
    {
        public static void ConvertBuiltinToURPMaterials()
        {
            Converters.RunInBatchMode(
                ConverterContainerId.BuiltInToURP
                , new List<ConverterId> {
                    ConverterId.Material,
                    ConverterId.ReadonlyMaterial
                }
                , ConverterFilter.Inclusive
            );
            EditorApplication.Exit(0);
        }
    }
    

To run the example conversion from the command line, use the following
command:

    
    
    "<path to Unity application> -projectPath <project path> -batchmode -executeMethod MyUpgradeScript.ConvertBuiltinToURPMaterials
    

Also check: [Unity Editor command line
arguments](https://docs.unity3d.com/Manual/EditorCommandLineArguments.html).

[](../../urp/upgrading-from-birp.html)

Upgrading from the Built-In Render Pipeline to URP

[](../../urp/upgrade-shaders-landing.html)

Upgrading shaders to URP from the Built-In Render Pipeline

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

