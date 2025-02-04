[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-share.html)
  * [中文](/cn/current/Manual/cus-share.html)
  * [日本語](/ja/current/Manual/cus-share.html)
  * [한국어](/kr/current/Manual/cus-share.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-share.html)
  * [中文](/cn/current/Manual/cus-share.html)
  * [日本語](/ja/current/Manual/cus-share.html)
  * [한국어](/kr/current/Manual/cus-share.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Sharing your package

[](cus-document.html)

Documenting your package

[](FeatureSets.html)

Feature sets

# Sharing your package

You can set up your own package registry server if you want to control package
access to a limited number of users, or if you need to set up package registry
servers in a closed network organization.

When you have finished developing your package and you want to share it with
other users, you have several options:  
  
---  
**Compressed file** | You can distribute a zip file to other Unity users. That way, they can decompress the zip file to a local folder on their own computer and [install the package from disk](upm-ui-local.html).  
**Tarball** | You can distribute a tarball to other Unity users. That way, they can [install the package from the local tarball](upm-ui-tarball.html) directly.  
**Git URL** | You can distribute a link to your Git repository, using one of the [supported protocols](upm-git.html). Then users can [install your package using its Git URL](upm-git.html), because the Unity Package Manager can fetch packages from Git repository hosting services like GitHub and GitLab.  
**Scoped Registry** | You can set up a package registry server to host your package and then publish it to that registry using the `npm` [publish command](https://docs.npmjs.com/creating-and-publishing-unscoped-public-packages). Your package’s consumers can then set up a [scoped registry](upm-scoped.html) configuration in their project to fetch your custom packages from your own package registry.  
  
Unity Package Manager supports registries based on the `npm` protocol. Make
sure that whatever registry server you choose implements the `/-/v1/search` or
`/-/all` endpoints.  
  
**Warning:** When you set up your own package registry server, make sure you
use only those features that are compatible with Unity’s Scoped Registries.
For example, Unity doesn’t support namespaces using the `@scope` notation that
`npm` supports.  
  
Most of the time, anonymous access within a local network is adequate to
fulfill your security requirements. However, if you want more control over who
accesses packages via scoped registries, you can enable [npm
authentication](https://docs.npmjs.com/about-authentication-tokens) for
specific users. Your package’s customers can then [configure their scoped
registries](upm-config-scoped.html) to use their npm authentication tokens.  
  
## Additional resources

  * [Creating custom packages](CustomPackages.html)
  * [Asset packages](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage)

[](cus-document.html)

Documenting your package

[](FeatureSets.html)

Feature sets

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

