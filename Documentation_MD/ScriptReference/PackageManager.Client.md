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

# Client

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

Use the Unity Package Manager Client class to manage the packages used in a
project.

**Note:** You can only call the Client methods in sequence. If you try to add
or remove multiple packages at the same time, the outcome is nondeterministic.
For example, if you call the [Remove](PackageManager.Client.Remove.html)
method on a package while a `Remove` operation is already in progress or
queued, might overwrite the current operation and only handle the latest
`Remove` operation.

### Static Properties

[LogLevel](PackageManager.Client.LogLevel.html)| Gets or sets the log level
that the Package Manager uses when logging to the Editor.log and upm.log
files. Defaults to LogLevel.Info.  
---|---  
  
### Static Methods

[Add](PackageManager.Client.Add.html)| Adds a package dependency to the
project. Requesting a new or different dependency often leads to changing
installed packages, but only after the Package Manager constructs a dependency
graph to solve any version conflicts. For more information, see Dependency and
resolution.  
---|---  
[AddAndRemove](PackageManager.Client.AddAndRemove.html)| Adds package
dependencies to the project and removes package dependencies from the project.
Requesting different dependencies often leads to changing installed packages,
but only after the Package Manager constructs a dependency graph to solve any
version conflicts. For more information, see Dependency and resolution.
Calling this function is much more efficient than calling the Add and Remove
functions several times because for this function, the Package Manager only
has to solve the dependency list once, instead of constructing a new
dependency graph after each call.  
[ClearCache](PackageManager.Client.ClearCache.html)| Empties the package
cache.  
[Embed](PackageManager.Client.Embed.html)|  Embeds a package inside the
project.  
[List](PackageManager.Client.List.html)| Lists the packages the project
depends on.  
[Pack](PackageManager.Client.Pack.html)| Creates a GZip tarball file from a
package folder. The format and content of the file is the same as if the
package was published to a package registry.  
[Remove](PackageManager.Client.Remove.html)| Removes a package dependency from
the project. Removing a dependency often leads to changing installed packages,
but only after the Package Manager constructs a dependency graph to solve any
version conflicts. For more information, see Dependency and resolution.  
[Resolve](PackageManager.Client.Resolve.html)| Forces the Package Manager to
resolve the project's packages, reinstalling any altered or missing package
and removing extraneous packages.  
[Search](PackageManager.Client.Search.html)| Searches for the given package.  
[SearchAll](PackageManager.Client.SearchAll.html)| Searches for all
discoverable packages compatible with the current Unity version.  
  
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

