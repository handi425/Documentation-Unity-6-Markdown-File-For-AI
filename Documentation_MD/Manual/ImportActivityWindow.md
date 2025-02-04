[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ImportActivityWindow.html)
  * [中文](/cn/current/Manual/ImportActivityWindow.html)
  * [日本語](/ja/current/Manual/ImportActivityWindow.html)
  * [한국어](/kr/current/Manual/ImportActivityWindow.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ImportActivityWindow.html)
  * [中文](/cn/current/Manual/ImportActivityWindow.html)
  * [日本語](/ja/current/Manual/ImportActivityWindow.html)
  * [한국어](/kr/current/Manual/ImportActivityWindow.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Import Activity window

[](SpecialFolders.html)

Reserved folder name reference

[](Presets.html)

Presets

# Import Activity window

## Overview

The Import Activity window provides you with information about what happens
when Unity imports your assets. You can use this information to identify which
assets in your project were imported recently, how long each asset took to
import, and why it was imported (or re-imported).

This information allows you to analyse your project’s import activity, and
make decisions about how to improve the time Unity takes to import your
assets, or how to avoid unnecessary imports altogether. The Import Activity
window therefore acts like a **profiler** A window that helps you to optimize
your game. It shows how much time is spent in the various areas of your game.
For example, it can report the percentage of time spent rendering, animating,
or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) for the import process.

## Accessing the Import Activity window

To open the Import Activity window, go to **Window > Analysis > Import
Activity Window**.

You can also open the Import Activity window directly from an asset, which
causes the window to immediately display the import details for the selected
asset. This is useful if you already know which asset’s import data you want
to analyse. There are two ways to do this:

  * Right-click an asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) and, from the context menu,
select **View in Import Activity Window**.

  * View an asset in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), right-click the Inspector’s tab,
and, from the context menu, select **Open in Import Activity Window**.

## Layout

The Import Activity window has three sections: the ****toolbar** A row of
buttons and basic controls at the top of the Unity Editor that allows you to
interact with the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) **at the top, the **asset list** on
the left, and the **information** section on the right.

![The layout of the import activity
window](../uploads/Main/ImportActivityLayout.png) The layout of the import
activity window

## Toolbar

![](../uploads/Main/ImportActivityToolbar.png)

The toolbar at the top of the window has the following three features:

  1. **Show overview** button
  2. **Options** menu
  3. Search field

### Show Overview button

When you click the **Show Overview** button, the information section on the
right displays overview information, which includes general information about
your asset imports. See Overview information, below.

### Options menu

The **Options** dropdown allows you to adjust the information shown in the
asset list. The following options are available:

#### Use relative timestamps

Controls whether the last import time is shown in relative format (eg. “a few
seconds ago”), or absolute format, in the form: **Day-Month-Year
Hour:Minute:Second**

#### Show previous imports

Controls whether previous imports are shown, or only the most recent import.
Showing previous imports allows you to see how many revisions of an asset are
currently being kept in the Library folder. This list is generally cleared
when Artifact Garbage Collection runs, when you restart the Editor.

When you enable this option, a second vertical list view appears alongside the
asset list, showing all the currently stored import results for the selected
asset.

![The previous imports list, showing three import results for the selected
asset.](../uploads/Main/ImportActivityPreviousImports.png) The **previous
imports** list, showing three import results for the selected asset.

If you want to keep import results from previous Editor sessions to aid with
debugging or analysis, you can turn off Artifact Garbage Collection by going
to **Project Settings > Editor > Remove unused Artifacts on Restart**. You can
also control this setting via script by using
`EditorUserSettings.artifactGarbageCollection`.

#### Include PreviewImporter

Controls whether to include artifacts generated by the preview window. These
are hidden by default, because they are not usually useful when examining your
asset imports.

### Search field

The search field on the right side of the toolbar allows you to quickly filter
the **asset list** by name to find the specific assets you are interested in.

## Asset list

The left-hand section of the window shows the list of all assets in your
project. The columns are:

  * **Asset** : The asset name 

  * **Last Import** : When the asset was last imported 

  * **Duration** : The amount of time the Last Import took, in milliseconds. 

To change the sort order of the list, click on the column headings.

![image alt text](../uploads/Main/ImportActivityAssetList.png) image alt text

_The asset list, with results shown sorted by longest duration first._

## Information panel

The right-hand section of the window is the information panel, and has two
modes:

  * Overview information appears when there is no asset selected. 

  * Asset information appears when you select an asset from the list on the left, or if you open the window directly via an asset as described above.

### Overview information

The Overview information displays a list of the assets with the most
dependencies, and assets with the longest import duration. It is useful for
quickly identifying which assets may be most significantly slowing down your
import process. Assets with more dependencies are more likely to be regularly
re-imported, because an asset is re-imported whenever any of its dependencies
are modified.

When you open the Import Activity window from the main menu, it displays the
Overview information by default. If you are viewing asset information and you
want to return to the Overview information, select the **Show overview**
button in the toolbar .

![The Import Activity window displaying the Overview on the right side, and
the Show Overview button in the top-left of the
window.](../uploads/Main/ImportActivityOverview.png) The Import Activity
window displaying the Overview on the right side, and the **_Show Overview_**
button in the top-left of the window.

### Asset information

![The asset information panel showing the information relating to a texture
asset.](../uploads/Main/ImportActivityAssetInfo.png) The asset information
panel showing the information relating to a texture asset.

When you select an asset from the asset list, the information panel displays
the asset information. This includes the following details about the asset and
its most recent import.

**Title** | **Description**  
---|---  
**Asset** | The name of the currently selected asset. You can click this field to locate the asset in the Project window.  
**GUID** | The unique GUID assigned to the asset. You can use this to track its references across your project.  
**Asset Size** | The size of the source file of the asset.  
**Path** | The file path of the asset, relative to the project’s root folder.  
**Editor Revision** | The version of the Editor that created this artifact.  
**Timestamp** | The time at which the Artifact file was created. This matches the timestamp value of the file in the `Library` folder.  
**Duration** | The time Unity took to import this asset in the most recent import, in milliseconds.  
**Reason for Import** | A description of the change (or changes) in your project which caused this asset’s most recent import, and details about the associated dependency type.  
  
The Reason for Import field has its own search bar, which allows you to search
its text. This is useful in situations where an asset has many reasons for
import (for example, a compute shader can have many dependencies that are
modified when you switch platforms).  
**Produced Files / Artifacts** | The list of files present in the `Library` folder that Unity produced when it last imported this asset. Usually there is just one artifact per asset, although sometimes there can be multiple. For example, when Unity generates a preview of an asset.  
  
During a typical usage of the Editor, Unity might generate many versions of an
asset’s import result (an artifact). For this reason, each artifact has an
artifact ID for reference. This is different to the asset’s GUID.  
  
The currently selected revision is referred to as the current revision, which
is selected by default when an asset in the Asset List is selected.  
  
Generally revisions are in chronological order with the current revision as
the newest. However, if you undo an operation in Unity which changes an
asset’s artifact, the current revision reverts back to a previously cached
artifact and therefore would not be the most recently listed artifact.  
**Dependencies** | A list of Editor and project-specific variables which control the state of an asset, which, if changed, trigger the re-import of the asset.  
  
Dependencies are how the asset database tracks the state of an asset. This
means that if an asset dependency changes, the import result will be different
and a new revision of an artifact will be generated.  
  
Understanding your asset’s dependency types and what can cause them to change
can help you get the most out of Unity’s asset database system, speed up your
workflow, and avoid unnecessary import time.  
  
This field has its own search bar, which allows you to search the text
contained in the Dependencies field.  
  
[](SpecialFolders.html)

Reserved folder name reference

[](Presets.html)

Presets

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

