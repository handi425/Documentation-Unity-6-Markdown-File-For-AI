[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-document.html)
  * [中文](/cn/current/Manual/cus-document.html)
  * [日本語](/ja/current/Manual/cus-document.html)
  * [한국어](/kr/current/Manual/cus-document.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-document.html)
  * [中文](/cn/current/Manual/cus-document.html)
  * [日本語](/ja/current/Manual/cus-document.html)
  * [한국어](/kr/current/Manual/cus-document.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Documenting your package

[](cus-legal.html)

Meeting legal requirements

[](cus-share.html)

Sharing your package

# Documenting your package

Most packages need some form of explanation to help users have the best
experience and optimize its use. This page provides some tips for how to
structure the information and format the documentation.

## Structure of the information

After the title of the package, give a basic overview of the package and its
contents. Following the overview and package contents, include instructions
for installing, system requirements, and limitations. You can also offer links
for getting help and providing feedback, including public forums or knowledge
bases, and support contacts.

After this preliminary information, you can offer more in-depth workflows,
description of the user interface or directory listings for samples, and then
more advanced topics. It’s best to offer reference pages near the end.

**Section** | **Description**  
---|---  
**Overview** | A brief, high-level explanation of the package.  
**Package contents** | Include the location of important files you want the user to know about. For example, if this is a sample package containing textures, models, and materials separated by sample group, you might want to specify the folder location of each group.  
**Installation instructions** | You can point to the official [Package Manager installation instructions](https://docs.unity3d.com/Manual/upm-ui-install.html), but if you have any special installation requirements, such as installing samples, add them here.  
**Requirements** | This is a good place to add hardware or software requirements, including which versions of the Unity Editor this package is compatible with.  
**Limitations** | If your package has any known limitations, you can list them here. If not, or if the limitations are trivial, exclude this section.  
**Workflows** | Include a list of steps that the user can follow that demonstrates how to use the feature. You can include screenshots to help describe how to use the feature.  
**Advanced topics** | Detailed information about what you’re providing to users. This is ideal if you don’t want to overwhelm the user with too much information up front.  
**Reference** | If you have a user interface with a lot of properties, you can describe their details in a reference section. Using tables is a good way to offer specific property descriptions.  
**Samples** | For packages that include sample files, you can include detailed information on how the user can use these sample files in their projects and **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).  
**Tutorials** | If you want to offer walkthroughs for complicated procedures, you can also add them here. Use step-by-step instructions and include images if they can help the user understand.  
  
## Documentation format

Markdown is a lightweight format commonly used in packages. Many repository
hosting services (such as GitHub and Bitbucket) support Markdown for `README`
files and documentation sites. You can include a Markdown file in the
`Documentation~` folder under your package root. Then, when a user clicks the
**Documentation** link in the [details panel](upm-ui-details.html) of Unity’s
Package Manager window, the user’s default Markdown viewer opens the file.

You can also use your own website to host your documentation. To set the
location for the **Documentation** link to point to your own website, set it
with the [documentationUrl](upm-manifestPkg.html#documentationUrl) property in
your `package.json` file.

If you decide to use Markdown to document your package, you can find
information about writing Markdown files from many sites, including:

  * The [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
  * [Bitbucket’s tutorial](https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html)
  * [GitHub’s Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[](cus-legal.html)

Meeting legal requirements

[](cus-share.html)

Sharing your package

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

