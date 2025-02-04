[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/APIUpdater.html)
  * [中文](/cn/current/Manual/APIUpdater.html)
  * [日本語](/ja/current/Manual/APIUpdater.html)
  * [한국어](/kr/current/Manual/APIUpdater.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/APIUpdater.html)
  * [中文](/cn/current/Manual/APIUpdater.html)
  * [日本語](/ja/current/Manual/APIUpdater.html)
  * [한국어](/kr/current/Manual/APIUpdater.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Upgrade Unity](UpgradeGuides.html)
  * API updater

[](UpgradeGuides.html)

Upgrade Unity

[](UpgradeGuideUnity6.html)

Upgrade to Unity 6

# API updater

To improve usability and performance, Unity might change the way classes,
functions and properties (the API) work. Occasionally, these improvements
might introduce breaking changes when moving from one major Unity version to
another.

To minimize the impact of breaking changes, the API updater identifies and
updates obsolete code in your **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) and assemblies.

The API updater consists of the ScriptUpdater and the AssemblyUpdater, which
are responsible for updating source code (scripts) and assemblies (dll files)
respectively.

**Note** : The API Updater can only fix certain errors and warnings in the
API. These are indicated as **UnityUpgradable** in the console message. You
must manually resolve other errors or warnings that the API Updater cannot
handle.

## Using the API updater

When a [script compilation](script-compilation.html) is triggered, the API
updater runs automatically. For example, this occurs when you:

  * Open a project.
  * Import a package.
  * Save changes to a script.

The API updater offers to update any obsolete code that it detects. If you
accept, it rewrites any obsolete code with the recommended updated version of
the API.

For example, the API updater would convert the following obsolete statement
from:

    
    
    light.color = Color.red;
    

to:

    
    
    GetComponent<Light>().color = Color.red;
    

The steps below describe the workflow of the API updater when Unity triggers a
script compilation:

  1. Unity triggers a script compilation.
  2. The API updater checks for updatable compiler errors or warnings that it can handle. 
     * If it doesn’t find any errors or warnings, the process ends.
     * If it finds any errors or warnings, it displays a dialog offering an automatic update.  
Close the Editor and back up your project before you let the API updater
update your scripts or assemblies. When you reopen your project, Unity
compiles your scripts and triggers the API updater.

  3. If you accept the update, the API updater updates all scripts in the same compilation unit.
  4. The API Updater repeats this process until it detects no more errors or warnings that it can handle.

The updater can run multiple times if scripts with obsolete code fall into
different compilation passes, for example, editor scripts.

If you don’t allow the API updater to update your scripts, the console
displays any script errors or warnings. Errors or warnings which the API
updater could resolve display (**UnityUpgradable**) in the message.

If your script has other errors which prevent the API updater from running
successfully, the Console displays a message to inform you of this. You must
resolve those errors before the API Updater can complete the updates.

## Command line arguments related to API Updater

When running Unity in batch mode from the command line, use the `-accept-
apiupdate` option to run the API updater. For more information, see [Command
Line Arguments](CommandLineArguments.html).

## Logging

The API updater logs changes it makes to any assemblies to the [Editor
log](log-files.html). To control how much information is logged, set the
UNITY_APIUPDATER_LOG_THRESHOLD environment variable to the desired log
threshold and start Unity. For example:

On Windows:

    
    
    c:> set UNITY_APIUPDATER_LOG_THRESHOLD=Debug
    c:> \path\to\unity\Unity.exe
    

On Linux:

    
    
    $ export UNITY_APIUPDATER_LOG_THRESHOLD=Debug
    $ /path/to/unity/Unity
    

On Mac:

    
    
    $ export UNITY_APIUPDATER_LOG_THRESHOLD=Debug
    $ /path/to/unity/Unity
    

**Note** : You can also use [version
control](https://en.wikipedia.org/wiki/Version_control)A system for managing
file changes. You can use Unity in conjunction with most common version
control tools, including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) to see changes the API updater
makes to a project’s scripts.

When AssemblyUpdater has finished, the Editor.log displays the changes. For
example:

    
    
    [AssemblyUpdater] Property access to 'UnityEngine.Rigidbody
    UnityEngine.GameObject::get_rigidbody()' in 'System.Void
    Test.ClassReferencingObsoleteUnityAPIThroughEditorAssembly::Run()' replaced with 'T
    UnityEngine.GameObject::GetComponent<UnityEngine.Rigidbody>()'.
    

The table below describes the values for the `UNITY_APIUPDATER_LOG_THRESHOLD`
environment variable:

Log threshold | Description  
---|---  
**Error** (default value) | The API updater only logs **Error** messages. Error messages are logged when the API updater fails to apply a specific update, which requires you to take corrective action (usually requesting the original assembly author to provide an updated version of the assembly).  
**Warning** | The API updater logs **Warning** and **Error** messages. Warning messages are logged when the API updater applies a change that the user might need to review.  
**Info** | The API updater logs **Informational** , **Warning** and **Error** messages. Info messages include updates applied by the AssemblyUpdater.  
**Debug** | The API updater logs all messages. This is useful for troubleshooting, for example if you have issues with the API updater that you want to report to Unity.  
  
## Troubleshooting

### API Updating failed. Check previous console messages.

The API updater couldn’t update all obsolete code. This can occur if the
updater can’t save its changes, for example if the user has read-only
permissions on the script.

Check the previous lines in the console to see any problems that occurred
during the update process.

  * 2018–07–31 Page amended 

  * “accept-apiupdate” command line option added in Unity 2017.2

  * AssemblyUpdater logging improved in Unity [2018.3](https://docs.unity3d.com/2018.3/Documentation/Manual/30_search.html?q=newin20183) NewIn20183

[](UpgradeGuides.html)

Upgrade Unity

[](UpgradeGuideUnity6.html)

Upgrade to Unity 6

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

