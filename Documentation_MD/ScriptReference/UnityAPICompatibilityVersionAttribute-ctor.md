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

# UnityAPICompatibilityVersionAttribute Constructor

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

## Declaration

public UnityAPICompatibilityVersionAttribute(string version, bool
checkOnlyUnityVersion);

### Parameters

version | Unity version that this assembly is compatible with.  
---|---  
checkOnlyUnityVersion | Must be set to true.  
  
### Description

Initializes a new instance of UnityAPICompatibilityVersionAttribute.

Use this overload during the development cycle to avoid the AssemblyUpdater
check that is performed on game code built outside of Unity and imported as
assemblies. You can also avoid this check by passing disable-assembly-updater
as a command line argument (see the Unity Manual for more details).

* * *

**Obsolete** This overload of the attribute has been deprecated. Use the
constructor that takes the version and a boolean.

## Declaration

public UnityAPICompatibilityVersionAttribute(string version);

### Parameters

version | Unity version that this assembly is compatible with.  
---|---  
  
### Description

Initializes a new instance of UnityAPICompatibilityVersionAttribute. This
overload has been deprecated.

* * *

## Declaration

public UnityAPICompatibilityVersionAttribute(string version, string[]
configurationAssembliesHashes);

### Parameters

version | Unity version that this assembly is compatible with.  
---|---  
configurationAssembliesHashes | A comma-separated list comprised of the assembly name and attribute hash pairs. For example, assemblyname:hash,assemblyname:hash.  
  
### Description

Initializes a new instance of UnityAPICompatibilityVersionAttribute. This
constructor is used by internal tooling.

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

