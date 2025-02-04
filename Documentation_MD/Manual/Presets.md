[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Presets.html)
  * [中文](/cn/current/Manual/Presets.html)
  * [日本語](/ja/current/Manual/Presets.html)
  * [한국어](/kr/current/Manual/Presets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Presets.html)
  * [中文](/cn/current/Manual/Presets.html)
  * [日本語](/ja/current/Manual/Presets.html)
  * [한국어](/kr/current/Manual/Presets.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Presets

[](ImportActivityWindow.html)

Import Activity window

[](SupportingPresets.html)

Supporting presets

# Presets

Presets are assets that you can use to save and apply identical property
settings across multiple components, assets, or [Project Settings](comp-
ManagerGroup.html) windows. You can also use Presets to specify default
settings for new components and default [import
settings](ImportingAssets.html) for assets in the [Preset Manager](class-
PresetManager.html). The Preset Manager supports any importers, components, or
scriptable objects you add to the Unity Editor.

You can only apply Presets in the Editor. Presets have no effect at runtime.
You can use scripting to [support presets](SupportingPresets.html) in your own
MonoBehaviour, ScriptableObject or ScriptedImporter classes.

## Saving and applying Presets

Presets allow you to save the property configuration of a component, asset, or
Project Settings window as a Preset asset. You can then use this Preset asset
to apply the same settings to a different component, asset, or Project
Settings window.

For example, you can edit the properties of a **Rigidbody** A component that
allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component, save these settings to a
Preset asset, then apply that Preset asset to Rigidbody components in other
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject). The other components in the
GameObjects aren’t affected. The Preset applies its settings only to the
Rigidbody component.

You can store Presets in the `Assets` folder of your project. Use the
[Project](ProjectView.html) window to view and select Presets to edit in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

![Example of Preset assets in the Project window, organized in a Presets
subfolder](../uploads/Main/PresetAssets.png) Example of Preset assets in the
**Project** window, organized in a _Presets_ subfolder

## Saving property settings to a Preset

Follow these instructions to save property settings to a Preset asset. You can
save property settings while in Edit mode or in Play mode.

  1. Select the GameObject, Asset import settings, or Project Settings window from which you want to reuse settings. When you select it, it appears in the **Inspector** window.

  2. In the **Inspector** window, configure the properties as you want to save them.

  3. Click the Preset selector (the slider icon) at the top-right of the **Inspector** window.   
![](../uploads/Main/preset-icon.png)

  4. In the Select Preset window, click **Create New**.   
![](../uploads/Main/presets-select-preset-window.png)  
A File Save dialog appears.

  5. Choose the location of your new Preset, enter its name, and click **Save**.

## Applying settings from a Preset

There are two ways to apply a Preset: the **Select Preset** window, or for
component Presets, you can also drag a Preset from the **Project** In Unity,
you use a project to design and develop a game. A project stores all of the
files that are related to a game, such as the asset and Scene files. [More
info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window onto the GameObject that
contains that component.

**Note:** Applying a Preset copies properties from the Preset to the item. It
doesn’t link the Preset to the item. Changes you make to the Preset don’t
affect the items you have previously applied the Preset to.

To apply a Preset via the **Select Preset** window:

  1. For GameObjects or assets you want to apply a Preset to, select them so that they appear in the **Inspector** window. For Project Settings that you want to apply a Preset to, open them in the **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window.

  2. In the **Inspector** , click the Preset selector (the slider icon).

  3. In the **Select Preset** window, search for and select the Preset to apply.

Unity applies this Preset to the component, asset, or Project Settings window.

  4. Close the **Select Preset** window.

If you apply a component Preset via drag-and-drop, Unity’s behavior depends on
the state of your GameObject:

  * If you drop the Preset on an existing GameObject in the Hierarchy window, Unity adds a new component and copies properties from the Preset.
  * If you drop the Preset on an empty area in the Hierarchy window, Unity creates a new, empty GameObject and adds a component with properties copied from the Preset.
  * If you drop the Preset on the Inspector window onto the title of an existing component, Unity copies properties from the Preset.
  * If you drop the Preset on an empty area in the Inspector window, Unity adds a new component and copies properties from the Preset.

### Applying partial Presets

You can choose to only apply some properties from a Preset and exclude others.
To do this:

  1. Select your Preset in the **Project** window.

  2. In the **Inspector** , right-click a property and choose **Exclude Property**. The window displays a red horizontal line next to excluded properties.  
![](../uploads/Main/preset-exclude-property.png)

  3. Apply the Preset to the target component, asset, or Project settings.

**Note:** To select all or clear all checkboxes in a Preset, select the **More
items** menu (**⋮**) or right-click the Preset name, and select **Include all
properties** or **Exclude all properties**. You can still adjust individual
properties if you need to.

You can also use the Exclude option for Presets that you then set as the
default configuration for components and asset importers. For more
information, refer to [Preset Manager](class-PresetManager.html).

## Editing a Preset

To edit a Preset asset, select it from the **Project** window and view it in
the **Inspector** window.

**Note:** When you change the properties in a Preset, your changes don’t
affect items you have already applied the Preset to. For example, if you apply
a Preset for a Rigidbody component to a GameObject, and then edit the Preset,
the settings in the Rigidbody component don’t change.

![Editing a Preset in the Inspector window](../uploads/Main/preset-edit-
preset.png) Editing a Preset in the Inspector window

## Importing Assets using Presets by folder

You can use a [script](DefaultPresetsByFolder.html) to apply a Preset to an
Asset based on the location of the Asset in the _Project_ window.

## Exporting Preset Assets

Use Presets to streamline your team’s workflows. You can even use Presets to
specify settings for [Project Settings](comp-ManagerGroup.html) windows,
including the **Preset** settings themselves. Use this feature to configure a
project then [export it](AssetPackagesCreate.html) as a custom **asset
package** A collection of files and data from Unity projects, or elements of
projects, which are compressed and stored in one file, similar to Zip files,
with the `.unitypackage` extension. Asset packages are a handy way of sharing
and re-using Unity projects and collections of assets. [More
info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage). Your team members can
[import](AssetPackagesImport.html) this asset package into their projects.

  1. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), select the Presets you want to
export .

  2. In the Unity menu, go to **Assets > Export Package**, or right-click inside the Project window and choose **Export Package**.  
The **Exporting package** window displays the items to export.

  3. If your Presets contain references to assets you want to include in the package, enable **Include dependencies**. This option includes **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that are **direct dependencies** A
**direct** dependency occurs when your project “requests” a specific package
version. To create a direct dependency, you add that package and version to
the **dependencies** property in your project manifest (expressed in the form
`package_name@package_version`). [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Directdependency) of the selected assets.

  4. If your Presets contain references to scripts that might depend on other scripts, enable **Include all scripts**. This option reduces the likelihood of compilation errors when using the exported package in another project.
  5. Click **Export**.
  6. Choose where you want to store the package, enter a file name, and click **Save**. Unity saves the package as a .unitypackage file.

## Using Presets for transitions of Animation State nodes

You can save and apply Presets for [Animation state](class-State.html) nodes.
However, the [transitions](class-Transition.html)The blend from one state to
another in a state machine, such as transitioning a character from a walk to a
jog animation. Transitions define how long the blend between states should
take, and the conditions that activate the blend. [More info](class-
Transition.html)  
See in [Glossary](Glossary.html#Transition) in the Preset are shared among
Presets and the nodes that you apply the Preset to. For example, you apply a
Preset to two different nodes in the [Animator window](AnimatorWindow.html)The
window where the Animator Controller is visualized and edited. [More
info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow). In the Inspector window, you
edit the settings for one of the transitions in the first node. Your change
also appears in the other node and in the Preset.

[](ImportActivityWindow.html)

Import Activity window

[](SupportingPresets.html)

Supporting presets

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

