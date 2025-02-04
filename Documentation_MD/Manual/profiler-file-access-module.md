[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-file-access-module.html)
  * [中文](/cn/current/Manual/profiler-file-access-module.html)
  * [日本語](/ja/current/Manual/profiler-file-access-module.html)
  * [한국어](/kr/current/Manual/profiler-file-access-module.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-file-access-module.html)
  * [中文](/cn/current/Manual/profiler-file-access-module.html)
  * [日本語](/ja/current/Manual/profiler-file-access-module.html)
  * [한국어](/kr/current/Manual/profiler-file-access-module.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * File Access Profiler module reference

[](ProfilerMemory.html)

Memory Profiler module reference

[](ProfilerGPU.html)

GPU Usage Profiler module

# File Access Profiler module reference

The File Access **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module displays information about
the file activity in your application, such as the number of read or write
operations Unity performs or the number of file handles open. The module can
display this information either for a specific frame or across all frames in a
capture. You can use this information to determine how efficiently your
application performs file operations.

The File Access module can capture information about file operations on any
file within your built application’s folder structure, or within your Unity
project folder if you run the Profiler in the Unity Editor. This module
doesn’t collect information about unsuccessful file operations. If a file
operation attempt is unsuccessful, Unity displays an error.

This module isn’t enabled by default. To enable the File Access Profiler
module, refer to [Activating Profiler modules](profiler-modules-
activate.html).

## Chart categories

The upper half of the Profiler window displays a File Access chart with the
following categories:

**Chart** | **Description**  
---|---  
**Files Opened** | The total number of files successfully opened in the local file system this frame.  
**Files Closed** | The total number of files successfully closed in the local file system this frame.  
**File Seeks** | The number of file seek operations performed in the local file system this frame. A file seek operation involves a search through the contents of a file.  
**Reads in Flight** | The total number of read operations that were in progress during this frame.  
**File Handles open** | The total number of file handles held open at any time during this frame. This includes files that Unity opens and closes within the same frame.  
  
## Module details pane toolbar

When you select a frame in the File Access Profiler module, the module details
pane displays detailed information about files that Unity accessed during the
capture. Use the **toolbar** A row of buttons and basic controls at the top of
the Unity Editor that allows you to interact with the Editor in various ways
(e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) to access the following
functionality:

**Property** | **Description**  
---|---  
**View dropdown** | Use the dropdown to change the view of the data:  
| **File Summary** | Displays a summary of all file activity for each file Unity accessed during the selected frame.  
| **Accesses** | Displays each file access operation in the data set in the order that they happened.  
**Frame dropdown** | Use the dropdown to choose how many frames to display file information for:  
| **This Frame** | Displays a summary of file activity for the selected frame.  
| **All Frames** | Displays a summary of file activity for all frames in the Profiler capture.  
**Analyze Markers** | This module doesn’t populate the details pane automatically. Select the Analyze Markers button to populate the details pane with data.  
  
## File Summary view

The File Summary view displays a summary of all file access operations that
happened to each file during the capture. One entry in the table represents
the full summary for a single file.

The following table describes all possible statistics that the File Summary
view table can display. Not all statistic columns are enabled by default. To
enable or disable a column, right-click anywhere in the row that contains the
column headers to open a menu. Use this menu to enable or disable the view of
each column.

**Value** | **Description**  
---|---  
**Filename** | The name of the file that was accessed.  
**Total Bytes Read** | Total number of bytes of information Unity read from this file during the selected frames.  
**Read Access Time (ms)** | Total time Unity spent performing reads from this file during the selected frames.  
**Access Count** | Total number of accesses of any type to this file during the selected frames.  
**First Frame** | The first frame that Unity accessed this file on.  
**Number of Frames** | Total number of frames that Unity accessed this file on.  
**ID** | An index that represents the order of execution of the file access markers.  
**Read Bandwidth (MBps)** | The average bandwidth of read operations on this file over the selected frames, in megabytes per second.  
**Open Count** | Total number of opening operations on this file during the selected frames.  
**Close Count** | Total number of closing operations on this file during the selected frames.  
**Read Count** | Total number of read operations on this file during the selected frames.  
**Write Count** | Total number of write operations on this file during the selected frames.  
**Seek Count** | Total number of file seek operations on this file during the selected frames.  
**Total Bytes Written** | The total number of bytes Unity wrote to this file during the selected frames.  
**Write Bandwidth (MBps)** | The average bandwidth of write operations on this file over the selected frames, in megabytes per second.  
**Open Access Time (ms)** | The total time Unity spent performing opening operations on this file during the selected frames, in milliseconds.  
**Close Access Time (ms)** | The total time Unity spent performing close operations on this file during the selected frames, in milliseconds.  
**Write Access Time (ms)** | The total time Unity spent performing write operations to this file during the selected frames, in milliseconds.  
**Total Access Time (ms)** | The total time Unity spent accessing this file during the selected frames, in milliseconds.  
  
## Accesses view

The Accesses view provides detailed information about every file access
operation in the capture. Each entry in the table in the details pane of the
Profiler represents a single file access operation to a single file. The
following table describes all possible columns that the Accesses view can
display.

**Value** | **Description**  
---|---  
**Index** | An ID number that represents the order in which Unity performed the access operations.  
**Filename** | The name of the accessed file during this operation. To view the file path in full, hover your cursor over the file name entry.  
**Type** | The type of access operation performed. This can be either Open, Close, Seek, Read, or Write.  
**Access Size** | The number of bytes transferred during the access, where the access was a read or write. Where the access was a file seek, the size is the destination offset.  
**Offset** | The (starting) offset of the file access.  
**Duration (ms)** | The time taken to perform this access, in milliseconds.  
**Average Bandwidth (MBps)** | The average bandwidth for this access, where the access type was a read.  
**First Frame Index** | The ID of the frame this access began on.  
**Frames** | The total number of frames this access occurred for.  
**Thread** | The thread the access occurred on.  
**Timestamp (ms)** | The time this access started, relative to the start of the profiler capture.  
  
## Context menu

Right-click on any of the file access markers to open a submenu with
additional options to explore the data. The available options are as follows:

**Value** | **Description**  
---|---  
**Show marker in timeline view** | Opens this marker in the [CPU Usage Profiler](ProfilerCPU.html) module.  
**Go to the first frame of this marker** | Selects the frame in which the marker first appears in the chart. This option is disabled if the marker only appears on one frame.  
**Go to the last frame of this marker** | Selects the frame in which this marker last appears in the chart. This option is disabled if the marker only appears on one frame.  
**Filter the view to this file path** | Populates the search bar with the contents of the **Filename** column to filter the results.  
  
## Additional resources

  * [Profiler modules introduction](profiler-modules-introduction.html)
  * [Profiler window reference](ProfilerWindow.html)
  * [Collect performance data introduction](profiling-collect-data-introduction.html)

[](ProfilerMemory.html)

Memory Profiler module reference

[](ProfilerGPU.html)

GPU Usage Profiler module

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

