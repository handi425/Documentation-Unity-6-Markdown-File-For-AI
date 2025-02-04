[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/perForceIntegration.html)
  * [中文](/cn/current/Manual/perForceIntegration.html)
  * [日本語](/ja/current/Manual/perForceIntegration.html)
  * [한국어](/kr/current/Manual/perForceIntegration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/perForceIntegration.html)
  * [中文](/cn/current/Manual/perForceIntegration.html)
  * [日本語](/ja/current/Manual/perForceIntegration.html)
  * [한국어](/kr/current/Manual/perForceIntegration.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Version Control](VersionControl.html)
  * Perforce Integration

[](Versioncontrolintegration.html)

Version control integrations

[](SmartMerge.html)

Smart merge

# Perforce Integration

For more information on **Perforce** , visit
[www.perforce.com](https://www.perforce.com/downloads/helix).

## Setting up Perforce

Follow the setup process described in the [Version
Control](Versioncontrolintegration.html)A system for managing file changes.
You can use Unity in conjunction with most common version control tools,
including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) documentation. See [Perforce
documentation](https://www.perforce.com/perforce/doc.current/manuals/p4v/) if
you encounter any problems.

**Note** : If your Perforce workspace has multi-factor authentication enabled
you will first need to login through the command line using _p4 login2_ or by
using a visual client like P4V to be able to login in the Unity Editor as
well.

## Working offline with Perforce

Only use this if you know how to work offline in Perforce without a Sandbox.
Refer to the [Perforce
documentation](https://www.perforce.com/manuals/p4v/Content/P4V/using.offline.html)
for further information.

## Troubleshooting

If Unity cannot commit your changes to Perforce (for example, if the server is
down, or you experience licensing issues), your changes are stored in a
separate changeset. If the console doesn’t list any info about the issue, you
can use the P4V client for Perforce to submit this changeset to see the exact
error message.

You cannot submit changes if you are sharing a workspace with another user. A
workspace should be dedicated to one user only.

## Automatic revert of unchanged files on submit

It’s possible to configure Perforce to revert unchanged files on submit. To do
this in P4V, select **Connection** > **Edit Current Workspace** , view the
**Advanced** tab and set the value of **On submit** to **Revert unchanged
files**.

[](Versioncontrolintegration.html)

Version control integrations

[](SmartMerge.html)

Smart merge

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

