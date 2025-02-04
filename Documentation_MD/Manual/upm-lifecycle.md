[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-lifecycle.html)
  * [中文](/cn/current/Manual/upm-lifecycle.html)
  * [日本語](/ja/current/Manual/upm-lifecycle.html)
  * [한국어](/kr/current/Manual/upm-lifecycle.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-lifecycle.html)
  * [中文](/cn/current/Manual/upm-lifecycle.html)
  * [日本語](/ja/current/Manual/upm-lifecycle.html)
  * [한국어](/kr/current/Manual/upm-lifecycle.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Concepts](upm-concepts.html)
  * Package states and lifecycle

[](upm-package-types.html)

Package types

[](upm-dependencies.html)

Dependency and resolution

# Package states and lifecycle

Starting from Unity Editor version 2021.1, a package can travel through the
following states during its lifecycle:

![Package lifecycle with Unity Package Manager](../uploads/Main/upm-
lifecycle_v2.svg) Package lifecycle with Unity Package Manager  
---  
**Birth** **(A)** | While the package developer creates the package, it’s in the **Custom** state.   
  
When it’s ready for Unity users to test it and provide feedback, a package
enters the [Experimental](pack-exp.html) state. Unity doesn’t support
experimental packages and doesn’t guarantee that experimental packages will be
fully released and verified to be safe to use in production until they enter
the release track.  
  
Experimental packages either use `0` as the major part of their version or the
`-exp.#` suffix on the patch part of their version. For example,
`mypackage@0.1.2` or `mypackage@1.2.3-exp.1`.  
  
**Release track** | When a package passes quality testing and contains no experimental features or functionality (including dependencies on experimental packages), it enters the [Pre-release](pack-preview.html) state, which is on the release track. Unity fully supports packages on the release track and commits to officially releasing them by the end of the current LTS cycle (for example, 2021.3) at the latest. For a list of pre-release packages available for this version, refer to [Pre-release packages](pack-preview.html).  
  
Unity’s release management only grants a package the [Released](pack-
safe.html) status after it passes several testing stages and validation
procedures, which also include checks for appropriate documentation,
changelog, and license files. Packages in this state never use non-numeric
suffixes as part of their version. For a list of released packages available
for this version, refer to [Released packages](pack-safe.html).  
  
If the package developer updates or changes a released package, that package
might return to another state depending on the severity:  
|  | **Type of change:** | **New state:** | **Version bump:**  
| **(B)** | Major API change that [breaks an API](upm-semver.html#asm-break) | Experimental |  `1.2.3` => `2.0.0-exp`  
| **(C)** | Minor API change that [doesn’t break the API but affects usage](upm-semver.html#asm-bcomp) | Pre-release |  `1.2.3` => `1.3.0-pre`  
| **(D)** | Bug fixes, trivial changes, and documentation updates typical of [patch updates](upm-semver.html#asm-none) | Released (same state) |  `1.2.3` => `1.2.4`  
**Death** **(E)** | Packages that reach their end of life are no longer supported in Editors where they’re marked **Deprecated**. Avoid using packages in a **Deprecated** state because they might be nonfunctional or unsafe.  
  
For more information, refer to [Deprecated packages](pack-deprecated.html).  
  
Some experimental packages go directly to the deprecated state without passing
through the release cycle track.  
  
The Package Manager window displays a [label](upm-ui-details.html#Tags) that
corresponds to some of these states.

**Note** : These package states only apply to packages that Unity develops
internally. Contact third-party package developers to ask about their specific
processes.

[](upm-package-types.html)

Package types

[](upm-dependencies.html)

Dependency and resolution

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

