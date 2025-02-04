[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-assets.html)
  * [中文](/cn/current/Manual/upm-assets.html)
  * [日本語](/ja/current/Manual/upm-assets.html)
  * [한국어](/kr/current/Manual/upm-assets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-assets.html)
  * [中文](/cn/current/Manual/upm-assets.html)
  * [日本語](/ja/current/Manual/upm-assets.html)
  * [한국어](/kr/current/Manual/upm-assets.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Scripting API for packages](upm-api.html)
  * Accessing package assets

[](upm-api.html)

Scripting API for packages

[](upm-scoped.html)

Scoped registries

# Accessing package assets

This section explains how to access or refer to assets that are defined inside
a package:

  * Referring to package paths
  * Loading a Texture inside a package
  * Resolving absolute paths

**Note** : Package Manager doesn’t support streaming assets in packages. Use
the
[Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
package instead.

## Referring to package paths

To refer to assets that are defined inside a package, use this path scheme:

    
    
    "Packages/<package-name>/..."
    

The path of the asset inside a package begins with `Packages/` and the package
[name](upm-manifestPkg.html#name) (not the [display name](upm-
manifestPkg.html#displayName)).

By contrast, you access project assets using this scheme:

    
    
    "Assets/..."
    

For example, the path for the file `image.png` in the package subfolder
`/Example/Images` of the **com.unity.images-library** package is:

    
    
    "Packages/com.unity.images-library/Example/Images/image.png"
    

To get the absolute path of an item in your `Packages` folder, you can use the
partial path as a parameter to the
[Path.GetFullPath()](https://docs.microsoft.com/en-
us/dotnet/api/system.io.path.getfullpath?view=netframework-4.7.2) method. For
an example, refer to Resolving absolute paths.

## Loading a Texture inside a package

To load a Texture stored inside a package, use the
[LoadAssetAtPath](../ScriptReference/AssetDatabase.LoadAssetAtPath.html)
method, which requires the `using UnityEditor` directive. Specify the path
following the `Packages/<package-name>/` path scheme as demonstrated in this
example:

    
    
    using UnityEditor;
    // ...
    Texture2D texture = (Texture2D)AssetDatabase.LoadAssetAtPath("Packages/com.unity.images-library/Example/Images/image.png", typeof(Texture2D));
    

## Resolving absolute paths

To get the absolute path of a packaged asset, use the
[Path.GetFullPath()](https://docs.microsoft.com/en-
us/dotnet/api/system.io.path.getfullpath?view=netframework-4.7.2) method,
which requires the `using System.IO` directive. For example:

    
    
    using System.IO;
    // ...
    string absolute =   Path.GetFullPath("Packages/com.unity.images-library/Example/Images/image.png");
    

## Additional resources

  * [PackageInfo.name](../ScriptReference/PackageManager.PackageInfo-name.html) (Scripting API)
  * [Search for files](search-files.html)

[](upm-api.html)

Scripting API for packages

[](upm-scoped.html)

Scoped registries

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

