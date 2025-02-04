[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# PackageInfo

class in UnityEditor.PackageManager

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-PackageManager.html "Go to PackageManager
Component in the Manual")

### Description

Structure describing a Unity Package.

Either a reference to a package in a registry, to a revision of a source
repository, a resource on the net or to a package available on disk.

### Properties

[assetPath](PackageManager.PackageInfo-assetPath.html)| The asset path of the
package in the AssetDatabase.  
---|---  
[author](PackageManager.PackageInfo-author.html)| An AuthorInfo instance of
the author of the package.  
[category](PackageManager.PackageInfo-category.html)| Category of the package.  
[changelogUrl](PackageManager.PackageInfo-changelogUrl.html)| The custom URL
for the changelog for the package.  
[datePublished](PackageManager.PackageInfo-datePublished.html)| The date and
time at which the package was published.  
[dependencies](PackageManager.PackageInfo-dependencies.html)| An array of
DependencyInfos listing all the packages this package directly depends on.  
[deprecationMessage](PackageManager.PackageInfo-deprecationMessage.html)|
Deprecation message for the version that this instance represents.  
[description](PackageManager.PackageInfo-description.html)| Detailed
description of the package.  
[displayName](PackageManager.PackageInfo-displayName.html)| Friendly display
name of the package.  
[documentationUrl](PackageManager.PackageInfo-documentationUrl.html)| The
custom URL for documentation for the package.  
[errors](PackageManager.PackageInfo-errors.html)| The errors associated with
the package.  
[git](PackageManager.PackageInfo-git.html)| A GitInfo instance providing
detailed information for a Git package.  
[isDeprecated](PackageManager.PackageInfo-isDeprecated.html)| Set to `true` if
the package version that this instance represents is deprecated.  
[isDirectDependency](PackageManager.PackageInfo-isDirectDependency.html)| If
the package is a direct dependency of the project.  
[keywords](PackageManager.PackageInfo-keywords.html)| An array of keywords
associated with the package.  
[licensesUrl](PackageManager.PackageInfo-licensesUrl.html)| The custom URL for
the licenses of a package.  
[name](PackageManager.PackageInfo-name.html)| Unique name of the package.  
[packageId](PackageManager.PackageInfo-packageId.html)| Identifier of the
package.  
[registry](PackageManager.PackageInfo-registry.html)| The registry where the
Package Manager might find this package.  
[repository](PackageManager.PackageInfo-repository.html)| A RepositoryInfo
instance containing information the repository that the package is hosted on.  
[resolvedDependencies](PackageManager.PackageInfo-resolvedDependencies.html)|
An array of DependencyInfo instances listing all the packages this package
directly or indirectly depends on and the versions they resolved to.  
[resolvedPath](PackageManager.PackageInfo-resolvedPath.html)| The local path
of the project on disk.  
[source](PackageManager.PackageInfo-source.html)| Source of the package
contents.  
[type](PackageManager.PackageInfo-type.html)| Type of the package.  
[version](PackageManager.PackageInfo-version.html)| Version of the package.  
[versions](PackageManager.PackageInfo-versions.html)| A VersionsInfo instance
containing information about the available versions of the package.  
  
### Static Methods

[FindForAssembly](PackageManager.PackageInfo.FindForAssembly.html)| Retrieves
information about the package containing an assembly, or the assembly
definition used to build that assembly.  
---|---  
[FindForAssetPath](PackageManager.PackageInfo.FindForAssetPath.html)|
Retrieves information about the package containing an asset based on the path
of that asset.  
[FindForPackageName](PackageManager.PackageInfo.FindForPackageName.html)|
Retrieves information about the package based on the name of that package.  
[GetAllRegisteredPackages](PackageManager.PackageInfo.GetAllRegisteredPackages.html)|
Retrieves information about all packages that are currently loaded.  
[IsPackageRegistered](PackageManager.PackageInfo.IsPackageRegistered.html)|
Checks if a specific package is registered with the UnityEditor.AssetDatabase.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

