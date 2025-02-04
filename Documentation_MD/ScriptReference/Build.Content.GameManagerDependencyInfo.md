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

# GameManagerDependencyInfo

struct in UnityEditor.Build.Content

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

[ ]()

### Description

Contains dependency information for internal Unity game manager classes. Call
[ContentBuildInterface.WriteGameManagersSerializedFile](Build.Content.ContentBuildInterface.WriteGameManagersSerializedFile.html)
or
[ContentBuildInterface.CalculatePlayerDependenciesForGameManagers](Build.Content.ContentBuildInterface.CalculatePlayerDependenciesForGameManagers.html)
to get an instance of this class.

Note: this class and its members exist to provide low-level support for the
**Scriptable Build Pipeline** package. This is intended for internal use only;
use the [Scriptable Build Pipeline
package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html)
to implement a fully featured build pipeline. You can install this via the
[Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-
manager-ui@latest/index.html).

### Properties

[includedTypes](Build.Content.GameManagerDependencyInfo-includedTypes.html)|
The project-wide identifiers for the game manager classes referenced in this
collection of dependency information.  
---|---  
[managerObjects](Build.Content.GameManagerDependencyInfo-managerObjects.html)|
The project-wide identifiers for the game manager classes referenced in this
collection of dependency information.  
[referencedObjects](Build.Content.GameManagerDependencyInfo-
referencedObjects.html)| The project-wide identifiers for any objects
referenced by the manager classes in the managerObjects list.  
  
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

