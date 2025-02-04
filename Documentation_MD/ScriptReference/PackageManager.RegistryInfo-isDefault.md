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

#  [RegistryInfo](PackageManager.RegistryInfo.html).isDefault

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

public bool isDefault;

### Description

Whether this is the default, Unity registry or one of the scoped registries
configured in the project manifest.

The default registry hosts the standard Unity packages. The Package Manager
always looks for packages in the default registry unless a project manifest
contains one or more scoped registries. When a manifest declares a scoped
registry, the Package Manager uses the scope to determine whether to look for
a package in that registry. You can configure scoped registries inside a
`scopedRegistries` element of your Project manifest file. All configured
registries must support the npm protocol.

    
    
    {
        "scopedRegistries": [
            {
                "name": "General",
                "url": "https://example.com/registry",
                "scopes": [ "com.example", "com.example.tools.physics"]
            }
        ],
        "dependencies": {
            "com.unity.animation": "1.0.0",
            "com.example.mycompany.tools.animation": "1.0.0",
            "com.example.animation": "1.0.0"
        }
    }

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

