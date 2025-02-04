[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-remove-local.html)
  * [中文](/cn/current/Manual/upm-ui-remove-local.html)
  * [日本語](/ja/current/Manual/upm-ui-remove-local.html)
  * [한국어](/kr/current/Manual/upm-ui-remove-local.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-remove-local.html)
  * [中文](/cn/current/Manual/upm-ui-remove-local.html)
  * [日本語](/ja/current/Manual/upm-ui-remove-local.html)
  * [한국어](/kr/current/Manual/upm-ui-remove-local.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Asset packages](AssetPackages.html)
  * Removing local asset packages

[](AssetPackagesImport.html)

Importing local asset packages

[](Archives.html)

Archives

# Removing local asset packages

When you import [local asset packages](AssetPackages.html), the Unity Editor
places them in the `Assets` directory in your project.

You can manually remove assets from a project if you know the assets aren’t in
use. You might consider this action to unclutter your project directory or to
free up space on your local hard drive.

**Warning** : Make sure your project isn’t using any of the assets you remove.
Unlike _installed_ packages, the Package Manager doesn’t track assets that you
_imported_ from local **asset packages** A collection of files and data from
Unity projects, or elements of projects, which are compressed and stored in
one file, similar to Zip files, with the `.unitypackage` extension. Asset
packages are a handy way of sharing and re-using Unity projects and
collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage), so it can’t detect when you
remove dependent assets.

## Before you begin

Make sure you understand these important notes before you begin:

  * Use this procedure to remove assets only if you added them to the current project by importing them by following the [Importing local asset packages](AssetPackagesImport.html) procedure. 
    * Don’t use this procedure to try to remove UPM packages that you installed from a registry. For information about removing packages that you installed from a registry, refer to [Remove a UPM package from a project](upm-ui-remove.html).
    * Don’t use this procedure to try to remove asset packages that you downloaded and imported to your project by using the Package Manager window. For information about removing asset packages that you downloaded and imported by using the Package Manager window, refer to [Remove imported assets from a project](upm-ui-remove-asset.html).
  * This procedure removes assets from the current project. It doesn’t remove the same assets that might exist in other projects.

## Procedure

To remove one or more local asset package items from your project:

  1. Open your project.

  2. Open the **Package Manager** window and [select a context](upm-ui-filter.html) from the [navigation panel](upm-ui-nav.html).

  3. Select the package you want to remove from your project and take note of the package name **(A)** and the publisher name **(B)**. These names might help you identify the asset directory in a later step.

![The My Assets context shows the package name \(A\) and the publisher name
\(B\)](../uploads/Main/upm-ui-myassets-details.png) The **My Assets** context
shows the package name (A) and the publisher name (B)

  4. Open the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow).

  5. Expand the `Assets` directory and locate the subdirectory for the package you identified in the **Package Manager** window in an earlier step.

  6. Explore the directory structure that the publisher created **(C)** , confirm it’s the correct package, and identify the assets you want to delete **(D)**. **Note** : Unity doesn’t impose directory names or structures on publishers, so their assets might not be in an easily identifiable directory. The directory structure might be simple or complex.

![The Project window with an assets folder selected \(C\) and its contents
\(D\)](../uploads/Main/upm-proj-assets.png) The Project window with an assets
folder selected (C) and its contents (D)

  7. Select the asset or assets you want to delete. Your selection can be a single asset, multiple assets, all assets in a subdirectory, or more.

  8. Right-click the selected items, and select **Delete**.

**Important** : **Scenes** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that depend on deleted assets aren’t
reported as errors in the **Console window** A Unity Editor window that shows
errors, warnings and other messages generated by Unity, or your own scripts.
[More info](Console.html)  
See in [Glossary](Glossary.html#Consolewindow). If you suspect the removal
caused issues, import the package again. Refer to [Download and import an
asset package](upm-ui-import.html).

## Additional resources

  * [Remove a UPM package from a project](upm-ui-remove.html)
  * [Remove imported assets from a project](upm-ui-remove-asset.html)

[](AssetPackagesImport.html)

Importing local asset packages

[](Archives.html)

Archives

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

