StatefulSets | Kubernetes
[Kubernetes](/)

* [Documentation](/docs/home/)
* [Kubernetes Blog](/blog/)
* [Training](/training/)
* [Careers](/careers/)
* [Partners](/partners/)
* [Community](/community/)
* [Versions](#)

  [Release Information](/releases)
  [v1.36](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  [v1.35](https://v1-35.docs.kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  [v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  [v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  [v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
* [English](#)

  [中文 (Chinese)](/zh-cn/docs/concepts/workloads/controllers/statefulset/)
  [Français (French)](/fr/docs/concepts/workloads/controllers/statefulset/)
  [Bahasa Indonesia (Indonesian)](/id/docs/concepts/workloads/controllers/statefulset/)
  [日本語 (Japanese)](/ja/docs/concepts/workloads/controllers/statefulset/)
  [한국어 (Korean)](/ko/docs/concepts/workloads/controllers/statefulset/)
  [Español (Spanish)](/es/docs/concepts/workloads/controllers/statefulset/)
  বাংলা (Bengali)
  [বাংলা (Bengali)](/bn/) 
  Deutsch (German)
  [Deutsch (German)](/de/) 
  हिन्दी (Hindi)
  [हिन्दी (Hindi)](/hi/) 
  Italiano (Italian)
  [Italiano (Italian)](/it/) 
  Polski (Polish)
  [Polski (Polish)](/pl/) 
  Português (Portuguese)
  [Português (Portuguese)](/pt-br/) 
  Русский (Russian)
  [Русский (Russian)](/ru/) 
  Українська (Ukrainian)
  [Українська (Ukrainian)](/uk/) 
  Tiếng Việt (Vietnamese)
  [Tiếng Việt (Vietnamese)](/vi/)

# StatefulSets

[English](#)

[বাংলা (Bengali)](/bn/docs/concepts/)
[中文 (Chinese)](/zh-cn/docs/concepts/)
[Français (French)](/fr/docs/concepts/)
[Deutsch (German)](/de/docs/concepts/)
[हिन्दी (Hindi)](/hi/docs/concepts/)
[Bahasa Indonesia (Indonesian)](/id/docs/concepts/)
[Italiano (Italian)](/it/docs/concepts/)
[日本語 (Japanese)](/ja/docs/concepts/)
[한국어 (Korean)](/ko/docs/concepts/)
[Polski (Polish)](/pl/docs/concepts/)
[Português (Portuguese)](/pt-br/docs/concepts/)
[Русский (Russian)](/ru/docs/concepts/)
[Español (Spanish)](/es/docs/concepts/)
[Українська (Ukrainian)](/uk/docs/concepts/)
[Tiếng Việt (Vietnamese)](/vi/docs/concepts/)

* [Kubernetes Documentation](/docs/ "Documentation")
  + [Documentation](/docs/home/ "Kubernetes Documentation")
    - [Available Documentation Versions](/docs/home/supported-doc-versions/)
  + [Getting started](/docs/setup/)
    - [Learning environment](/docs/setup/learning-environment/)
    - [Production environment](/docs/setup/production-environment/)
      * [Container Runtimes](/docs/setup/production-environment/container-runtimes/)
      * [Installing Kubernetes with deployment tools](/docs/setup/production-environment/tools/)
        + [Bootstrapping clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/)
          - [Installing kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
          - [Troubleshooting kubeadm](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
          - [Creating a cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
          - [Customizing components with the kubeadm API](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
          - [Options for Highly Available Topology](/docs/setup/production-environment/tools/kubeadm/ha-topology/)
          - [Creating Highly Available Clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/)
          - [Set up a High Availability etcd Cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)
          - [Configuring each kubelet in your cluster using kubeadm](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)
          - [Dual-stack support with kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
      * [Turnkey Cloud Solutions](/docs/setup/production-environment/turnkey-solutions/)
    - [Best practices](/docs/setup/best-practices/)
      * [Considerations for large clusters](/docs/setup/best-practices/cluster-large/)
      * [Running in multiple zones](/docs/setup/best-practices/multiple-zones/)
      * [Validate node setup](/docs/setup/best-practices/node-conformance/)
      * [Enforcing Pod Security Standards](/docs/setup/best-practices/enforcing-pod-security-standards/)
      * [PKI certificates and requirements](/docs/setup/best-practices/certificates/)
  + [Concepts](/docs/concepts/)
    - [Overview](/docs/concepts/overview/)
      * [Kubernetes Components](/docs/concepts/overview/components/)
      * [Objects In Kubernetes](/docs/concepts/overview/working-with-objects/)
        + [Kubernetes Object Management](/docs/concepts/overview/working-with-objects/object-management/)
        + [Object Names and IDs](/docs/concepts/overview/working-with-objects/names/)
        + [Labels and Selectors](/docs/concepts/overview/working-with-objects/labels/)
        + [Namespaces](/docs/concepts/overview/working-with-objects/namespaces/)
        + [Annotations](/docs/concepts/overview/working-with-objects/annotations/)
        + [Field Selectors](/docs/concepts/overview/working-with-objects/field-selectors/)
        + [Finalizers](/docs/concepts/overview/working-with-objects/finalizers/)
        + [Owners and Dependents](/docs/concepts/overview/working-with-objects/owners-dependents/)
        + [Recommended Labels](/docs/concepts/overview/working-with-objects/common-labels/)
        + [Storage Versions](/docs/concepts/overview/working-with-objects/storage-version/)
      * [The Kubernetes API](/docs/concepts/overview/kubernetes-api/)
      * [The kubectl command-line tool](/docs/concepts/overview/kubectl/)
    - [Cluster Architecture](/docs/concepts/architecture/)
      * [Nodes](/docs/concepts/architecture/nodes/)
      * [Communication between Nodes and the Control Plane](/docs/concepts/architecture/control-plane-node-communication/)
      * [Controllers](/docs/concepts/architecture/controller/)
      * [Leases](/docs/concepts/architecture/leases/)
      * [Cloud Controller Manager](/docs/concepts/architecture/cloud-controller/)
      * [About cgroup v2](/docs/concepts/architecture/cgroups/)
      * [Kubernetes Self-Healing](/docs/concepts/architecture/self-healing/)
      * [Garbage Collection](/docs/concepts/architecture/garbage-collection/)
      * [Mixed Version Proxy](/docs/concepts/architecture/mixed-version-proxy/)
    - [Containers](/docs/concepts/containers/)
      * [Images](/docs/concepts/containers/images/)
      * [Container Environment](/docs/concepts/containers/container-environment/)
      * [Runtime Class](/docs/concepts/containers/runtime-class/)
      * [Container Lifecycle Hooks](/docs/concepts/containers/container-lifecycle-hooks/)
      * [Container Runtime Interface (CRI)](/docs/concepts/containers/cri/)
    - [Workloads](/docs/concepts/workloads/)
      * [Pods](/docs/concepts/workloads/pods/)
        + [Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/)
        + [Pod Conditions](/docs/concepts/workloads/pods/pod-condition/)
        + [Init Containers](/docs/concepts/workloads/pods/init-containers/)
        + [Sidecar Containers](/docs/concepts/workloads/pods/sidecar-containers/)
        + [Ephemeral Containers](/docs/concepts/workloads/pods/ephemeral-containers/)
        + [Disruptions](/docs/concepts/workloads/pods/disruptions/)
        + [Pod Hostname](/docs/concepts/workloads/pods/pod-hostname/)
        + [Pod Quality of Service Classes](/docs/concepts/workloads/pods/pod-qos/)
        + [Scheduling Group](/docs/concepts/workloads/pods/scheduling-group/)
        + [User Namespaces](/docs/concepts/workloads/pods/user-namespaces/)
        + [Downward API](/docs/concepts/workloads/pods/downward-api/)
        + [Advanced Pod Configuration](/docs/concepts/workloads/pods/advanced-pod-config/)
      * [Workload API](/docs/concepts/workloads/workload-api/)
        + [Pod Group Disruption and Priority](/docs/concepts/workloads/workload-api/disruption-and-priority/)
        + [PodGroup Scheduling Policies](/docs/concepts/workloads/workload-api/policies/)
        + [Topology-Aware Workload Scheduling](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
      * [Workload Management](/docs/concepts/workloads/controllers/)
        + [Deployments](/docs/concepts/workloads/controllers/deployment/)
        + [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
        + [StatefulSets](/docs/concepts/workloads/controllers/statefulset/)
        + [DaemonSet](/docs/concepts/workloads/controllers/daemonset/)
        + [Jobs](/docs/concepts/workloads/controllers/job/)
        + [Automatic Cleanup for Finished Jobs](/docs/concepts/workloads/controllers/ttlafterfinished/)
        + [CronJob](/docs/concepts/workloads/controllers/cron-jobs/)
        + [ReplicationController](/docs/concepts/workloads/controllers/replicationcontroller/)
      * [PodGroup API](/docs/concepts/workloads/podgroup-api/)
        + [PodGroup Lifecycle](/docs/concepts/workloads/podgroup-api/lifecycle/)
      * [Managing Workloads](/docs/concepts/workloads/management/)
      * [Autoscaling Workloads](/docs/concepts/workloads/autoscaling/)
      * [Horizontal Pod Autoscaling](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
      * [Resource managers](/docs/concepts/workloads/resource-managers/)
      * [Vertical Pod Autoscaling](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
    - [Services, Load Balancing, and Networking](/docs/concepts/services-networking/)
      * [Service](/docs/concepts/services-networking/service/)
      * [Ingress](/docs/concepts/services-networking/ingress/)
      * [Ingress Controllers](/docs/concepts/services-networking/ingress-controllers/)
      * [Gateway API](/docs/concepts/services-networking/gateway/)
      * [EndpointSlices](/docs/concepts/services-networking/endpoint-slices/)
      * [Network Policies](/docs/concepts/services-networking/network-policies/)
      * [DNS for Services and Pods](/docs/concepts/services-networking/dns-pod-service/)
      * [IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/)
      * [Topology Aware Routing](/docs/concepts/services-networking/topology-aware-routing/)
      * [Networking on Windows](/docs/concepts/services-networking/windows-networking/)
      * [Service ClusterIP allocation](/docs/concepts/services-networking/cluster-ip-allocation/)
      * [Service Internal Traffic Policy](/docs/concepts/services-networking/service-traffic-policy/)
    - [Storage](/docs/concepts/storage/)
      * [Volumes](/docs/concepts/storage/volumes/)
      * [Persistent Volumes](/docs/concepts/storage/persistent-volumes/)
      * [Projected Volumes](/docs/concepts/storage/projected-volumes/)
      * [Ephemeral Volumes](/docs/concepts/storage/ephemeral-volumes/)
      * [Storage Classes](/docs/concepts/storage/storage-classes/)
      * [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)
      * [Dynamic Volume Provisioning](/docs/concepts/storage/dynamic-provisioning/)
      * [Volume Snapshots](/docs/concepts/storage/volume-snapshots/)
      * [Volume Snapshot Classes](/docs/concepts/storage/volume-snapshot-classes/)
      * [CSI Volume Cloning](/docs/concepts/storage/volume-pvc-datasource/)
      * [Storage Capacity](/docs/concepts/storage/storage-capacity/)
      * [Node-specific Volume Limits](/docs/concepts/storage/storage-limits/)
      * [Local ephemeral storage](/docs/concepts/storage/ephemeral-storage/)
      * [Volume Health Monitoring](/docs/concepts/storage/volume-health-monitoring/)
      * [Windows Storage](/docs/concepts/storage/windows-storage/)
    - [Configuration](/docs/concepts/configuration/)
      * [ConfigMaps](/docs/concepts/configuration/configmap/)
      * [Secrets](/docs/concepts/configuration/secret/)
      * [Liveness, Readiness, and Startup Probes](/docs/concepts/configuration/liveness-readiness-startup-probes/)
      * [Resource Management for Pods and Containers](/docs/concepts/configuration/manage-resources-containers/)
      * [Organizing Cluster Access Using kubeconfig Files](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
      * [Resource Management for Windows nodes](/docs/concepts/configuration/windows-resource-management/)
    - [Security](/docs/concepts/security/)
      * [Cloud Native Security](/docs/concepts/security/cloud-native-security/ "Cloud Native Security and Kubernetes")
      * [Pod Security Standards](/docs/concepts/security/pod-security-standards/)
      * [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
      * [Service Accounts](/docs/concepts/security/service-accounts/)
      * [Pod Security Policies](/docs/concepts/security/pod-security-policy/)
      * [Security For Linux Nodes](/docs/concepts/security/linux-security/)
      * [Security For Windows Nodes](/docs/concepts/security/windows-security/)
      * [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/)
      * [Role Based Access Control Good Practices](/docs/concepts/security/rbac-good-practices/)
      * [Good practices for Kubernetes Secrets](/docs/concepts/security/secrets-good-practices/)
      * [Multi-tenancy](/docs/concepts/security/multi-tenancy/)
      * [Hardening Guide - Authentication Mechanisms](/docs/concepts/security/hardening-guide/authentication-mechanisms/)
      * [Hardening Guide - Dynamic Resource Allocation](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
      * [Hardening Guide - Scheduler Configuration](/docs/concepts/security/hardening-guide/scheduler/)
      * [Kubernetes API Server Bypass Risks](/docs/concepts/security/api-server-bypass-risks/)
      * [Linux kernel security constraints for Pods and containers](/docs/concepts/security/linux-kernel-security-constraints/)
      * [Security Checklist](/docs/concepts/security/security-checklist/)
      * [Application Security Checklist](/docs/concepts/security/application-security-checklist/)
    - [Policies](/docs/concepts/policy/)
      * [Limit Ranges](/docs/concepts/policy/limit-range/)
      * [Resource Quotas](/docs/concepts/policy/resource-quotas/)
      * [Process ID Limits And Reservations](/docs/concepts/policy/pid-limiting/)
    - [Scheduling, Preemption and Eviction](/docs/concepts/scheduling-eviction/)
      * [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
      * [Topology-Aware Workload Scheduling](/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
      * [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
      * [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
      * [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
      * [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
      * [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
      * [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework/)
      * [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
      * [Gang Scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/)
      * [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
      * [PodGroup Scheduling](/docs/concepts/scheduling-eviction/podgroup-scheduling/)
      * [Resource Bin Packing](/docs/concepts/scheduling-eviction/resource-bin-packing/)
      * [Workload-Aware Preemption](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
      * [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
      * [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
      * [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
      * [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/)
    - [Cluster Administration](/docs/concepts/cluster-administration/)
      * [Node Shutdowns](/docs/concepts/cluster-administration/node-shutdown/)
      * [Swap memory management](/docs/concepts/cluster-administration/swap-memory-management/)
      * [Node Autoscaling](/docs/concepts/cluster-administration/node-autoscaling/)
      * [Certificates](/docs/concepts/cluster-administration/certificates/)
      * [Cluster Networking](/docs/concepts/cluster-administration/networking/)
      * [Observability](/docs/concepts/cluster-administration/observability/)
      * [Admission Webhook Good Practices](/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
      * [Good practices for Dynamic Resource Allocation as a Cluster Admin](/docs/concepts/cluster-administration/dra/)
      * [Logging Architecture](/docs/concepts/cluster-administration/logging/)
      * [Compatibility Version For Kubernetes Control Plane Components](/docs/concepts/cluster-administration/compatibility-version/)
      * [Metrics For Kubernetes System Components](/docs/concepts/cluster-administration/system-metrics/)
      * [Metrics for Kubernetes Object States](/docs/concepts/cluster-administration/kube-state-metrics/)
      * [System Logs](/docs/concepts/cluster-administration/system-logs/)
      * [Traces For Kubernetes System Components](/docs/concepts/cluster-administration/system-traces/)
      * [Proxies in Kubernetes](/docs/concepts/cluster-administration/proxies/)
      * [API Priority and Fairness](/docs/concepts/cluster-administration/flow-control/)
      * [Installing Addons](/docs/concepts/cluster-administration/addons/)
      * [Coordinated Leader Election](/docs/concepts/cluster-administration/coordinated-leader-election/)
    - [Windows in Kubernetes](/docs/concepts/windows/)
      * [Windows containers in Kubernetes](/docs/concepts/windows/intro/)
      * [Guide for Running Windows Containers in Kubernetes](/docs/concepts/windows/user-guide/)
    - [Extending Kubernetes](/docs/concepts/extend-kubernetes/)
      * [Compute, Storage, and Networking Extensions](/docs/concepts/extend-kubernetes/compute-storage-net/)
        + [Network Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
        + [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
      * [Extending the Kubernetes API](/docs/concepts/extend-kubernetes/api-extension/)
        + [Custom Resources](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
        + [Kubernetes API Aggregation Layer](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
      * [Operator pattern](/docs/concepts/extend-kubernetes/operator/)
  + [Tasks](/docs/tasks/)
    - [Install Tools](/docs/tasks/tools/)
      * [Install and Set Up kubectl on Linux](/docs/tasks/tools/install-kubectl-linux/)
      * [Install and Set Up kubectl on macOS](/docs/tasks/tools/install-kubectl-macos/)
      * [Install and Set Up kubectl on Windows](/docs/tasks/tools/install-kubectl-windows/)
    - [Administer a Cluster](/docs/tasks/administer-cluster/)
      * [Administration with kubeadm](/docs/tasks/administer-cluster/kubeadm/)
        + [Adding Linux worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
        + [Adding Windows worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
        + [Upgrading kubeadm clusters](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
        + [Upgrading Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
        + [Upgrading Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
        + [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
        + [Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
        + [Reconfiguring a kubeadm cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/)
        + [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
      * [Overprovision Node Capacity For A Cluster](/docs/tasks/administer-cluster/node-overprovisioning/)
      * [Migrating from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)
        + [Changing the Container Runtime on a Node from Docker Engine to containerd](/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/)
        + [Find Out What Container Runtime is Used on a Node](/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/)
        + [Troubleshooting CNI plugin-related errors](/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
        + [Check whether dockershim removal affects you](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
        + [Migrating telemetry and security agents from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)
      * [Generate Certificates Manually](/docs/tasks/administer-cluster/certificates/)
      * [Manage Memory, CPU, and API Resources](/docs/tasks/administer-cluster/manage-resources/)
        + [Configure Default Memory Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
        + [Configure Default CPU Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
        + [Configure Minimum and Maximum Memory Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
        + [Configure Minimum and Maximum CPU Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
        + [Configure Memory and CPU Quotas for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
        + [Configure a Pod Quota for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
      * [Install a Network Policy Provider](/docs/tasks/administer-cluster/network-policy-provider/)
        + [Use Antrea for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/)
        + [Use Calico for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
        + [Use Cilium for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
        + [Use Kube-router for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)
        + [Romana for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/)
        + [Weave Net for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/)
      * [Access Clusters Using the Kubernetes API](/docs/tasks/administer-cluster/access-cluster-api/)
      * [Enable Or Disable Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/)
      * [Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/)
      * [Autoscale the DNS Service in a Cluster](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
      * [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)
      * [Change the default StorageClass](/docs/tasks/administer-cluster/change-default-storage-class/)
      * [Switching from Polling to CRI Event-based Updates to Container Status](/docs/tasks/administer-cluster/switch-to-evented-pleg/)
      * [Change the Reclaim Policy of a PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
      * [Cloud Controller Manager Administration](/docs/tasks/administer-cluster/running-cloud-controller/)
      * [Configure a kubelet image credential provider](/docs/tasks/administer-cluster/kubelet-credential-provider/)
      * [Configure Quotas for API Objects](/docs/tasks/administer-cluster/quota-api-object/)
      * [Control CPU Management Policies on the Node](/docs/tasks/administer-cluster/cpu-management-policies/)
      * [Control Memory Management Policies on a Node](/docs/tasks/administer-cluster/memory-manager/)
      * [Control Topology Management Policies on a node](/docs/tasks/administer-cluster/topology-manager/)
      * [Customizing DNS Service](/docs/tasks/administer-cluster/dns-custom-nameservers/)
      * [Debugging DNS Resolution](/docs/tasks/administer-cluster/dns-debugging-resolution/)
      * [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/)
      * [Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/)
      * [Enable Or Disable A Kubernetes API](/docs/tasks/administer-cluster/enable-disable-api/)
      * [Encrypting Confidential Data at Rest](/docs/tasks/administer-cluster/encrypt-data/)
      * [Decrypt Confidential Data that is Already Encrypted at Rest](/docs/tasks/administer-cluster/decrypt-data/)
      * [Guaranteed Scheduling For Critical Add-On Pods](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)
      * [IP Masquerade Agent User Guide](/docs/tasks/administer-cluster/ip-masq-agent/)
      * [Limit Storage Consumption](/docs/tasks/administer-cluster/limit-storage-consumption/)
      * [Migrate Replicated Control Plane To Use Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/)
      * [Operating etcd clusters for Kubernetes](/docs/tasks/administer-cluster/configure-upgrade-etcd/)
      * [Reserve Compute Resources for System Daemons](/docs/tasks/administer-cluster/reserve-compute-resources/)
      * [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/)
      * [Safely Drain a Node](/docs/tasks/administer-cluster/safely-drain-node/)
      * [Securing a Cluster](/docs/tasks/administer-cluster/securing-a-cluster/)
      * [Harden Dynamic Resource Allocation in Your Cluster](/docs/tasks/administer-cluster/hardening-dra/)
      * [Set Kubelet Parameters Via A Configuration File](/docs/tasks/administer-cluster/kubelet-config-file/)
      * [Share a Cluster with Namespaces](/docs/tasks/administer-cluster/namespaces/)
      * [Upgrade A Cluster](/docs/tasks/administer-cluster/cluster-upgrade/)
      * [Use Cascading Deletion in a Cluster](/docs/tasks/administer-cluster/use-cascading-deletion/)
      * [Using a KMS provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)
      * [Using CoreDNS for Service Discovery](/docs/tasks/administer-cluster/coredns/)
      * [Using NodeLocal DNSCache in Kubernetes Clusters](/docs/tasks/administer-cluster/nodelocaldns/)
      * [Using sysctls in a Kubernetes Cluster](/docs/tasks/administer-cluster/sysctl-cluster/)
      * [Verify Signed Kubernetes Artifacts](/docs/tasks/administer-cluster/verify-signed-artifacts/)
    - [Configure Pods and Containers](/docs/tasks/configure-pod-container/)
      * [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
      * [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)
      * [Assign Devices to Pods and Containers](/docs/tasks/configure-pod-container/assign-resources/)
        + [Set Up DRA in a Cluster](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/)
        + [Allocate Devices to Workloads with DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
        + [Access DRA Device Metadata](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)
      * [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)
      * [Configure GMSA for Windows Pods and containers](/docs/tasks/configure-pod-container/configure-gmsa/)
      * [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)
      * [Resize CPU and Memory Resources assigned to Pods](/docs/tasks/configure-pod-container/resize-pod-resources/)
      * [Configure RunAsUserName for Windows pods and containers](/docs/tasks/configure-pod-container/configure-runasusername/)
      * [Create a Windows HostProcess Pod](/docs/tasks/configure-pod-container/create-hostprocess-pod/)
      * [Configure Quality of Service for Pods](/docs/tasks/configure-pod-container/quality-service-pod/)
      * [Assign Extended Resources to a Container](/docs/tasks/configure-pod-container/extended-resource/)
      * [Configure a Pod to Use a Volume for Storage](/docs/tasks/configure-pod-container/configure-volume-storage/)
      * [Configure a Pod to Use a Projected Volume for Storage](/docs/tasks/configure-pod-container/configure-projected-volume-storage/)
      * [Configure a Security Context for a Pod or Container](/docs/tasks/configure-pod-container/security-context/)
      * [Configure Service Accounts for Pods](/docs/tasks/configure-pod-container/configure-service-account/)
      * [Pull an Image from a Private Registry](/docs/tasks/configure-pod-container/pull-image-private-registry/)
      * [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
      * [Assign Pods to Nodes](/docs/tasks/configure-pod-container/assign-pods-nodes/)
      * [Assign Pods to Nodes using Node Affinity](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
      * [Configure Pod Initialization](/docs/tasks/configure-pod-container/configure-pod-initialization/)
      * [Attach Handlers to Container Lifecycle Events](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)
      * [Configure a Pod to Use a ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)
      * [Share Process Namespace between Containers in a Pod](/docs/tasks/configure-pod-container/share-process-namespace/)
      * [Use a User Namespace With a Pod](/docs/tasks/configure-pod-container/user-namespaces/)
      * [Use an Image Volume With a Pod](/docs/tasks/configure-pod-container/image-volumes/)
      * [Create static Pods](/docs/tasks/configure-pod-container/static-pod/)
      * [Translate a Docker Compose File to Kubernetes Resources](/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
      * [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/)
      * [Enforce Pod Security Standards with Namespace Labels](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
      * [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/)
    - [Monitoring, Logging, and Debugging](/docs/tasks/debug/)
      * [Logging in Kubernetes](/docs/tasks/debug/logging/)
      * [Monitoring in Kubernetes](/docs/tasks/debug/monitoring/)
      * [Troubleshooting Applications](/docs/tasks/debug/debug-application/)
        + [Debug Pods](/docs/tasks/debug/debug-application/debug-pods/)
        + [Debug Services](/docs/tasks/debug/debug-application/debug-service/)
        + [Debug a StatefulSet](/docs/tasks/debug/debug-application/debug-statefulset/)
        + [Determine the Reason for Pod Failure](/docs/tasks/debug/debug-application/determine-reason-pod-failure/)
        + [Debug Init Containers](/docs/tasks/debug/debug-application/debug-init-containers/)
        + [Debug Running Pods](/docs/tasks/debug/debug-application/debug-running-pod/)
        + [Get a Shell to a Running Container](/docs/tasks/debug/debug-application/get-shell-running-container/)
      * [Troubleshooting Clusters](/docs/tasks/debug/debug-cluster/)
        + [Troubleshooting kubectl](/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/)
        + [Resource metrics pipeline](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
        + [Tools for Monitoring Resources](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
        + [Monitor Node Health](/docs/tasks/debug/debug-cluster/monitor-node-health/)
        + [Debugging Kubernetes nodes with crictl](/docs/tasks/debug/debug-cluster/crictl/)
        + [Troubleshooting Topology Management](/docs/tasks/debug/debug-cluster/topology/)
        + [Auditing](/docs/tasks/debug/debug-cluster/audit/)
        + [Debugging Kubernetes Nodes With Kubectl](/docs/tasks/debug/debug-cluster/kubectl-node-debug/)
        + [Developing and debugging services locally using telepresence](/docs/tasks/debug/debug-cluster/local-debugging/)
        + [Windows debugging tips](/docs/tasks/debug/debug-cluster/windows/)
    - [Manage Kubernetes Objects](/docs/tasks/manage-kubernetes-objects/)
      * [Declarative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/declarative-config/)
      * [Declarative Management of Kubernetes Objects Using Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/)
      * [Managing Kubernetes Objects Using Imperative Commands](/docs/tasks/manage-kubernetes-objects/imperative-command/)
      * [Imperative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/imperative-config/)
      * [Update API Objects in Place Using kubectl patch](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)
      * [Migrate Kubernetes Objects Using Storage Version Migration](/docs/tasks/manage-kubernetes-objects/storage-version-migration/)
    - [Managing Secrets](/docs/tasks/configmap-secret/)
      * [Managing Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
      * [Managing Secrets using Configuration File](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
      * [Managing Secrets using Kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)
    - [Inject Data Into Applications](/docs/tasks/inject-data-application/)
      * [Define a Command and Arguments for a Container](/docs/tasks/inject-data-application/define-command-argument-container/)
      * [Define Dependent Environment Variables](/docs/tasks/inject-data-application/define-interdependent-environment-variables/)
      * [Define Environment Variables for a Container](/docs/tasks/inject-data-application/define-environment-variable-container/)
      * [Define Environment Variable Values Using An Init Container](/docs/tasks/inject-data-application/define-environment-variable-via-file/)
      * [Expose Pod Information to Containers Through Environment Variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
      * [Expose Pod Information to Containers Through Files](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
      * [Distribute Credentials Securely Using Secrets](/docs/tasks/inject-data-application/distribute-credentials-secure/)
    - [Run Applications](/docs/tasks/run-application/)
      * [Run a Stateless Application Using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
      * [Horizontal Manual Scaling for a Deployment](/docs/tasks/run-application/scale-deployment/)
      * [Update a Deployment Without Downtime](/docs/tasks/run-application/update-deployment-rolling/)
      * [Run a Single-Instance Stateful Application](/docs/tasks/run-application/run-single-instance-stateful-application/)
      * [Run a Replicated Stateful Application](/docs/tasks/run-application/run-replicated-stateful-application/)
      * [Scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/)
      * [Delete a StatefulSet](/docs/tasks/run-application/delete-stateful-set/)
      * [Force Delete StatefulSet Pods](/docs/tasks/run-application/force-delete-stateful-set-pod/)
      * [HorizontalPodAutoscaler Walkthrough](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
      * [Specifying a Disruption Budget for your Application](/docs/tasks/run-application/configure-pdb/)
      * [Accessing the Kubernetes API from a Pod](/docs/tasks/run-application/access-api-from-pod/)
    - [Run Jobs](/docs/tasks/job/)
      * [Running Automated Tasks with a CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)
      * [Coarse Parallel Processing Using a Work Queue](/docs/tasks/job/coarse-parallel-processing-work-queue/)
      * [Fine Parallel Processing Using a Work Queue](/docs/tasks/job/fine-parallel-processing-work-queue/)
      * [Indexed Job for Parallel Processing with Static Work Assignment](/docs/tasks/job/indexed-parallel-processing-static/)
      * [Job with Pod-to-Pod Communication](/docs/tasks/job/job-with-pod-to-pod-communication/)
      * [Parallel Processing using Expansions](/docs/tasks/job/parallel-processing-expansion/)
      * [Handling retriable and non-retriable pod failures with Pod failure policy](/docs/tasks/job/pod-failure-policy/)
    - [Access Applications in a Cluster](/docs/tasks/access-application-cluster/)
      * [Deploy and Access the Kubernetes Dashboard](/docs/tasks/access-application-cluster/web-ui-dashboard/)
      * [Accessing Clusters](/docs/tasks/access-application-cluster/access-cluster/)
      * [Configure Access to Multiple Clusters](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
      * [Use Port Forwarding to Access Applications in a Cluster](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
      * [Use a Service to Access an Application in a Cluster](/docs/tasks/access-application-cluster/service-access-application-cluster/)
      * [Connect a Frontend to a Backend Using Services](/docs/tasks/access-application-cluster/connecting-frontend-backend/)
      * [Create an External Load Balancer](/docs/tasks/access-application-cluster/create-external-load-balancer/)
      * [List All Container Images Running in a Cluster](/docs/tasks/access-application-cluster/list-all-running-container-images/)
      * [Communicate Between Containers in the Same Pod Using a Shared Volume](/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)
      * [Configure DNS for a Cluster](/docs/tasks/access-application-cluster/configure-dns-cluster/)
      * [Access Services Running on Clusters](/docs/tasks/access-application-cluster/access-cluster-services/)
    - [Extend Kubernetes](/docs/tasks/extend-kubernetes/)
      * [Configure the Aggregation Layer](/docs/tasks/extend-kubernetes/configure-aggregation-layer/)
      * [Use Custom Resources](/docs/tasks/extend-kubernetes/custom-resources/)
        + [Extend the Kubernetes API with CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
        + [Versions in CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
      * [Set up an Extension API Server](/docs/tasks/extend-kubernetes/setup-extension-api-server/)
      * [Configure Multiple Schedulers](/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)
      * [Use an HTTP Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/http-proxy-access-api/)
      * [Use a SOCKS5 Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/socks5-proxy-access-api/)
      * [Set up Konnectivity service](/docs/tasks/extend-kubernetes/setup-konnectivity/)
    - [TLS](/docs/tasks/tls/)
      * [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/)
      * [Configure Certificate Rotation for the Kubelet](/docs/tasks/tls/certificate-rotation/)
      * [Manage TLS Certificates in a Cluster](/docs/tasks/tls/managing-tls-in-a-cluster/)
      * [Manual Rotation of CA Certificates](/docs/tasks/tls/manual-rotation-of-ca-certificates/)
    - [Manage Cluster Daemons](/docs/tasks/manage-daemon/)
      * [Building a Basic DaemonSet](/docs/tasks/manage-daemon/create-daemon-set/)
      * [Perform a Rolling Update on a DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/)
      * [Perform a Rollback on a DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/)
      * [Running Pods on Only Some Nodes](/docs/tasks/manage-daemon/pods-some-nodes/)
    - [Networking](/docs/tasks/network/)
      * [Adding entries to Pod /etc/hosts with HostAliases](/docs/tasks/network/customize-hosts-file-for-pods/)
      * [Extend Service IP Ranges](/docs/tasks/network/extend-service-ip-ranges/)
      * [Kubernetes Default ServiceCIDR Reconfiguration](/docs/tasks/network/reconfigure-default-service-ip-ranges/)
      * [Validate IPv4/IPv6 dual-stack](/docs/tasks/network/validate-dual-stack/)
    - [Extend kubectl with plugins](/docs/tasks/extend-kubectl/kubectl-plugins/)
    - [Manage HugePages](/docs/tasks/manage-hugepages/scheduling-hugepages/)
    - [Schedule GPUs](/docs/tasks/manage-gpus/scheduling-gpus/)
  + [Tutorials](/docs/tutorials/)
    - [Hello Minikube](/docs/tutorials/hello-minikube/)
    - [Learn Kubernetes Basics](/docs/tutorials/kubernetes-basics/)
      * [Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/)
        + [Using Minikube to Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)
      * [Deploy an App](/docs/tutorials/kubernetes-basics/deploy-app/)
        + [Using kubectl to Create a Deployment](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
      * [Explore Your App](/docs/tutorials/kubernetes-basics/explore/)
        + [Viewing Pods and Nodes](/docs/tutorials/kubernetes-basics/explore/explore-intro/)
      * [Expose Your App Publicly](/docs/tutorials/kubernetes-basics/expose/)
        + [Using a Service to Expose Your App](/docs/tutorials/kubernetes-basics/expose/expose-intro/)
      * [Scale Your App](/docs/tutorials/kubernetes-basics/scale/)
        + [Running Multiple Instances of Your App](/docs/tutorials/kubernetes-basics/scale/scale-intro/)
      * [Update Your App](/docs/tutorials/kubernetes-basics/update/)
        + [Performing a Rolling Update](/docs/tutorials/kubernetes-basics/update/update-intro/)
    - [Configuration](/docs/tutorials/configuration/)
      * [Updating Configuration via a ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/)
      * [Configuring Redis using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)
      * [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)
      * [Configure a Pod to Use a PersistentVolume for Storage](/docs/tutorials/configuration/configure-persistent-volume-storage/)
    - [Security](/docs/tutorials/security/)
      * [Apply Pod Security Standards at the Cluster Level](/docs/tutorials/security/cluster-level-pss/)
      * [Apply Pod Security Standards at the Namespace Level](/docs/tutorials/security/ns-level-pss/)
      * [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
      * [Restrict a Container's Syscalls with seccomp](/docs/tutorials/security/seccomp/)
    - [Stateless Applications](/docs/tutorials/stateless-application/)
      * [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
      * [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)
    - [Stateful Applications](/docs/tutorials/stateful-application/)
      * [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
      * [Example: Deploying WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
      * [Example: Deploying Cassandra with a StatefulSet](/docs/tutorials/stateful-application/cassandra/)
      * [Running ZooKeeper, A Distributed System Coordinator](/docs/tutorials/stateful-application/zookeeper/)
    - [Cluster Management](/docs/tutorials/cluster-management/)
      * [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
      * [Configuring swap memory on Kubernetes nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
      * [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)
      * [Namespaces Walkthrough](/docs/tutorials/cluster-management/namespaces-walkthrough/)
    - [Services](/docs/tutorials/services/)
      * [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
      * [Using Source IP](/docs/tutorials/services/source-ip/)
      * [Explore Termination Behavior for Pods And Their Endpoints](/docs/tutorials/services/pods-and-endpoint-termination-flow/)
  + [Reference](/docs/reference/)
    - [Glossary](/docs/reference/glossary/)
    - [API Overview](/docs/reference/using-api/)
      * [Declarative API Validation](/docs/reference/using-api/declarative-validation/)
      * [Kubernetes API Concepts](/docs/reference/using-api/api-concepts/)
      * [Server-Side Apply](/docs/reference/using-api/server-side-apply/)
      * [Client Libraries](/docs/reference/using-api/client-libraries/)
      * [Common Expression Language in Kubernetes](/docs/reference/using-api/cel/)
      * [Kubernetes Deprecation Policy](/docs/reference/using-api/deprecation-policy/)
      * [Deprecated API Migration Guide](/docs/reference/using-api/deprecation-guide/)
      * [Kubernetes API health endpoints](/docs/reference/using-api/health-checks/)
    - [API Access Control](/docs/reference/access-authn-authz/)
      * [Authenticating](/docs/reference/access-authn-authz/authentication/)
      * [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
      * [Authorization](/docs/reference/access-authn-authz/authorization/)
      * [Using RBAC Authorization](/docs/reference/access-authn-authz/rbac/)
      * [Using Node Authorization](/docs/reference/access-authn-authz/node/)
      * [Webhook Mode](/docs/reference/access-authn-authz/webhook/)
      * [Using ABAC Authorization](/docs/reference/access-authn-authz/abac/)
      * [Admission Control](/docs/reference/access-authn-authz/admission-controllers/ "Admission Control in Kubernetes")
      * [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
      * [Managing Service Accounts](/docs/reference/access-authn-authz/service-accounts-admin/)
      * [User Impersonation](/docs/reference/access-authn-authz/user-impersonation/)
      * [Certificates and Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
      * [Mapping PodSecurityPolicies to Pod Security Standards](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
      * [Kubelet authentication/authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
      * [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
      * [Manifest-Based Admission Control](/docs/reference/access-authn-authz/manifest-admission-control/)
      * [Mutating Admission Policy](/docs/reference/access-authn-authz/mutating-admission-policy/)
      * [Validating Admission Policy](/docs/reference/access-authn-authz/validating-admission-policy/)
    - [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/)
      * [Audit Annotations](/docs/reference/labels-annotations-taints/audit-annotations/)
    - [Kubernetes API](/docs/reference/kubernetes-api/)
      * [Workload Resources](/docs/reference/kubernetes-api/workload-resources/)
        + [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)
        + [Binding](/docs/reference/kubernetes-api/workload-resources/binding-v1/)
        + [PodTemplate](/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)
        + [PodGroup v1alpha2](/docs/reference/kubernetes-api/workload-resources/pod-group-v1alpha2/)
        + [ReplicationController](/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)
        + [ReplicaSet](/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
        + [Deployment](/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
        + [StatefulSet](/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
        + [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/)
        + [DaemonSet](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/)
        + [Job](/docs/reference/kubernetes-api/workload-resources/job-v1/)
        + [CronJob](/docs/reference/kubernetes-api/workload-resources/cron-job-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)
        + [PriorityClass](/docs/reference/kubernetes-api/workload-resources/priority-class-v1/)
        + [DeviceTaintRule v1beta2](/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1beta2/)
        + [ResourceClaim](/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/)
        + [ResourceClaimTemplate](/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/)
        + [ResourceSlice](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1/)
        + [Workload v1alpha2](/docs/reference/kubernetes-api/workload-resources/workload-v1alpha2/)
      * [Service Resources](/docs/reference/kubernetes-api/service-resources/)
        + [Service](/docs/reference/kubernetes-api/service-resources/service-v1/)
        + [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
        + [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/)
        + [Ingress](/docs/reference/kubernetes-api/service-resources/ingress-v1/)
        + [IngressClass](/docs/reference/kubernetes-api/service-resources/ingress-class-v1/)
      * [Config and Storage Resources](/docs/reference/kubernetes-api/config-and-storage-resources/)
        + [ConfigMap](/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)
        + [Secret](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
        + [CSIDriver](/docs/reference/kubernetes-api/config-and-storage-resources/csi-driver-v1/)
        + [CSINode](/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/)
        + [CSIStorageCapacity](/docs/reference/kubernetes-api/config-and-storage-resources/csi-storage-capacity-v1/)
        + [PersistentVolumeClaim](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
        + [PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
        + [StorageClass](/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/)
        + [StorageVersionMigration v1beta1](/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1beta1/)
        + [Volume](/docs/reference/kubernetes-api/config-and-storage-resources/volume/)
        + [VolumeAttachment](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)
        + [VolumeAttributesClass](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attributes-class-v1/)
      * [Authentication Resources](/docs/reference/kubernetes-api/authentication-resources/)
        + [ServiceAccount](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)
        + [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
        + [TokenReview](/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)
        + [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)
        + [ClusterTrustBundle v1beta1](/docs/reference/kubernetes-api/authentication-resources/cluster-trust-bundle-v1beta1/)
        + [SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/)
        + [PodCertificateRequest v1beta1](/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1beta1/)
      * [Authorization Resources](/docs/reference/kubernetes-api/authorization-resources/)
        + [LocalSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/local-subject-access-review-v1/)
        + [SelfSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-access-review-v1/)
        + [SelfSubjectRulesReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/)
        + [SubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/)
        + [ClusterRole](/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)
        + [ClusterRoleBinding](/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)
        + [Role](/docs/reference/kubernetes-api/authorization-resources/role-v1/)
        + [RoleBinding](/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)
      * [Policy Resources](/docs/reference/kubernetes-api/policy-resources/)
        + [FlowSchema](/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/)
        + [LimitRange](/docs/reference/kubernetes-api/policy-resources/limit-range-v1/)
        + [ResourceQuota](/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/)
        + [NetworkPolicy](/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
        + [PodDisruptionBudget](/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)
        + [PriorityLevelConfiguration](/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/)
        + [ValidatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-v1/)
        + [ValidatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-binding-v1/)
        + [MutatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-v1/)
        + [MutatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-binding-v1/)
      * [Extend Resources](/docs/reference/kubernetes-api/extend-resources/)
        + [CustomResourceDefinition](/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/)
        + [DeviceClass](/docs/reference/kubernetes-api/extend-resources/device-class-v1/)
        + [MutatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/)
        + [ValidatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/)
      * [Cluster Resources](/docs/reference/kubernetes-api/cluster-resources/)
        + [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/)
        + [ComponentStatus](/docs/reference/kubernetes-api/cluster-resources/component-status-v1/)
        + [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1/)
        + [IPAddress](/docs/reference/kubernetes-api/cluster-resources/ip-address-v1/)
        + [Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/)
        + [LeaseCandidate v1beta1](/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/)
        + [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
        + [Node](/docs/reference/kubernetes-api/cluster-resources/node-v1/)
        + [RuntimeClass](/docs/reference/kubernetes-api/cluster-resources/runtime-class-v1/)
        + [ResourcePoolStatusRequest v1alpha3](/docs/reference/kubernetes-api/cluster-resources/resource-pool-status-request-v1alpha3/)
        + [ServiceCIDR](/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/)
      * [Common Definitions](/docs/reference/kubernetes-api/common-definitions/)
        + [DeleteOptions](/docs/reference/kubernetes-api/common-definitions/delete-options/)
        + [LabelSelector](/docs/reference/kubernetes-api/common-definitions/label-selector/)
        + [ListMeta](/docs/reference/kubernetes-api/common-definitions/list-meta/)
        + [LocalObjectReference](/docs/reference/kubernetes-api/common-definitions/local-object-reference/)
        + [NodeSelectorRequirement](/docs/reference/kubernetes-api/common-definitions/node-selector-requirement/)
        + [ObjectFieldSelector](/docs/reference/kubernetes-api/common-definitions/object-field-selector/)
        + [ObjectMeta](/docs/reference/kubernetes-api/common-definitions/object-meta/)
        + [ObjectReference](/docs/reference/kubernetes-api/common-definitions/object-reference/)
        + [Patch](/docs/reference/kubernetes-api/common-definitions/patch/)
        + [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/)
        + [ResourceFieldSelector](/docs/reference/kubernetes-api/common-definitions/resource-field-selector/)
        + [Status](/docs/reference/kubernetes-api/common-definitions/status/)
        + [TypedLocalObjectReference](/docs/reference/kubernetes-api/common-definitions/typed-local-object-reference/)
      * [Common Parameters](/docs/reference/kubernetes-api/common-parameters/common-parameters/)
    - [Instrumentation](/docs/reference/instrumentation/)
      * [Service Level Indicator Metrics](/docs/reference/instrumentation/slis/ "Kubernetes Component SLI Metrics")
      * [CRI Pod & Container Metrics](/docs/reference/instrumentation/cri-pod-container-metrics/)
      * [Native Histograms](/docs/reference/instrumentation/native-histograms/ "Native Histogram Support for Kubernetes Metrics")
      * [Node metrics data](/docs/reference/instrumentation/node-metrics/)
      * [Understand Pressure Stall Information (PSI) Metrics](/docs/reference/instrumentation/understand-psi-metrics/)
      * [Kubernetes z-pages](/docs/reference/instrumentation/zpages/)
      * [Kubernetes Metrics Reference](/docs/reference/instrumentation/metrics/)
    - [Kubernetes Issues and Security](/docs/reference/issues-security/)
      * [Kubernetes Issue Tracker](/docs/reference/issues-security/issues/)
      * [Kubernetes Security and Disclosure Information](/docs/reference/issues-security/security/)
      * [CVE feed](/docs/reference/issues-security/official-cve-feed/ "Official CVE Feed")
    - [Node Reference Information](/docs/reference/node/)
      * [Kubelet Checkpoint API](/docs/reference/node/kubelet-checkpoint-api/)
      * [Linux Kernel Version Requirements](/docs/reference/node/kernel-version-requirements/)
      * [Articles on dockershim Removal and on Using CRI-compatible Runtimes](/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/)
      * [Kubelet Pod Info gRPC API](/docs/reference/node/kubelet-pod-info-grpc-api/)
      * [Node Labels Populated By The Kubelet](/docs/reference/node/node-labels/)
      * [Kubelet Sync Loop](/docs/reference/node/kubelet-sync-loop/)
      * [Local Files And Paths Used By The Kubelet](/docs/reference/node/kubelet-files/)
      * [Kubelet Configuration Directory Merging](/docs/reference/node/kubelet-config-directory-merging/)
      * [Kubelet Device Manager API Versions](/docs/reference/node/device-plugin-api-versions/)
      * [Kubelet Systemd Watchdog](/docs/reference/node/systemd-watchdog/)
      * [Node Status](/docs/reference/node/node-status/)
      * [Seccomp and Kubernetes](/docs/reference/node/seccomp/)
      * [Linux Node Swap Behaviors](/docs/reference/node/swap-behavior/)
    - [Networking Reference](/docs/reference/networking/)
      * [Protocols for Services](/docs/reference/networking/service-protocols/)
      * [Ports and Protocols](/docs/reference/networking/ports-and-protocols/)
      * [Virtual IPs and Service Proxies](/docs/reference/networking/virtual-ips/)
    - [Setup tools](/docs/reference/setup-tools/)
      * [Kubeadm](/docs/reference/setup-tools/kubeadm/)
        + [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/)
        + [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/)
        + [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/)
        + [kubeadm upgrade phases](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/)
        + [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/)
        + [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/)
        + [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/)
        + [kubeadm version](/docs/reference/setup-tools/kubeadm/kubeadm-version/)
        + [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/)
        + [kubeadm certs](/docs/reference/setup-tools/kubeadm/kubeadm-certs/)
        + [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/)
        + [kubeadm join phase](/docs/reference/setup-tools/kubeadm/kubeadm-join-phase/)
        + [kubeadm kubeconfig](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/)
        + [kubeadm reset phase](/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/)
        + [Implementation details](/docs/reference/setup-tools/kubeadm/implementation-details/)
    - [Command line tool (kubectl)](/docs/reference/kubectl/)
      * [Introduction to kubectl](/docs/reference/kubectl/introduction/)
      * [kubectl Quick Reference](/docs/reference/kubectl/quick-reference/)
      * [kubectl reference](/docs/reference/kubectl/generated/)
        + [kubectl](/docs/reference/kubectl/generated/kubectl/)
        + [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/)
        + [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/)
        + [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/)
        + [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/)
          - [kubectl apply edit-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_edit-last-applied/)
          - [kubectl apply set-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_set-last-applied/)
          - [kubectl apply view-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_view-last-applied/)
        + [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/)
        + [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/)
          - [kubectl auth can-i](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
          - [kubectl auth reconcile](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_reconcile/)
          - [kubectl auth whoami](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/)
        + [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/)
        + [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/)
          - [kubectl certificate approve](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/)
          - [kubectl certificate deny](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_deny/)
        + [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/)
          - [kubectl cluster-info dump](/docs/reference/kubectl/generated/kubectl_cluster-info/kubectl_cluster-info_dump/)
        + [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/)
        + [kubectl config](/docs/reference/kubectl/generated/kubectl_config/)
          - [kubectl config current-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_current-context/)
          - [kubectl config delete-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-cluster/)
          - [kubectl config delete-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-context/)
          - [kubectl config delete-user](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-user/)
          - [kubectl config get-clusters](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-clusters/)
          - [kubectl config get-contexts](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts/)
          - [kubectl config get-users](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-users/)
          - [kubectl config rename-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/)
          - [kubectl config set](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set/)
          - [kubectl config set-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-cluster/)
          - [kubectl config set-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/)
          - [kubectl config set-credentials](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials/)
          - [kubectl config unset](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_unset/)
          - [kubectl config use-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_use-context/)
          - [kubectl config view](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_view/)
        + [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/)
        + [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/)
        + [kubectl create](/docs/reference/kubectl/generated/kubectl_create/)
          - [kubectl create clusterrole](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrole/)
          - [kubectl create clusterrolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrolebinding/)
          - [kubectl create configmap](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/)
          - [kubectl create cronjob](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_cronjob/)
          - [kubectl create deployment](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/)
          - [kubectl create ingress](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_ingress/)
          - [kubectl create job](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_job/)
          - [kubectl create namespace](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/)
          - [kubectl create poddisruptionbudget](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_poddisruptionbudget/)
          - [kubectl create priorityclass](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_priorityclass/)
          - [kubectl create quota](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_quota/)
          - [kubectl create role](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/)
          - [kubectl create rolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_rolebinding/)
          - [kubectl create secret](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret/)
          - [kubectl create secret docker-registry](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_docker-registry/)
          - [kubectl create secret generic](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_generic/)
          - [kubectl create secret tls](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/)
          - [kubectl create service](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service/)
          - [kubectl create service clusterip](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_clusterip/)
          - [kubectl create service externalname](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_externalname/)
          - [kubectl create service loadbalancer](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_loadbalancer/)
          - [kubectl create service nodeport](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_nodeport/)
          - [kubectl create serviceaccount](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_serviceaccount/)
          - [kubectl create token](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/)
        + [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/)
        + [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/)
        + [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/)
        + [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/)
        + [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/)
        + [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/)
        + [kubectl events](/docs/reference/kubectl/generated/kubectl_events/)
        + [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/)
        + [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/)
        + [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/)
        + [kubectl get](/docs/reference/kubectl/generated/kubectl_get/)
        + [kubectl kuberc](/docs/reference/kubectl/generated/kubectl_kuberc/)
          - [kubectl kuberc set](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_set/)
          - [kubectl kuberc view](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_view/)
        + [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/)
        + [kubectl label](/docs/reference/kubectl/generated/kubectl_label/)
        + [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/)
        + [kubectl options](/docs/reference/kubectl/generated/kubectl_options/)
        + [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/)
        + [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/)
          - [kubectl plugin list](/docs/reference/kubectl/generated/kubectl_plugin/kubectl_plugin_list/)
        + [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/)
        + [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/)
        + [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/)
        + [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/)
          - [kubectl rollout history](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_history/)
          - [kubectl rollout pause](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_pause/)
          - [kubectl rollout restart](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart/)
          - [kubectl rollout resume](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_resume/)
          - [kubectl rollout status](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)
          - [kubectl rollout undo](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/)
        + [kubectl run](/docs/reference/kubectl/generated/kubectl_run/)
        + [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/)
        + [kubectl set](/docs/reference/kubectl/generated/kubectl_set/)
          - [kubectl set env](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_env/)
          - [kubectl set image](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_image/)
          - [kubectl set resources](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_resources/)
          - [kubectl set selector](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_selector/)
          - [kubectl set serviceaccount](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_serviceaccount/)
          - [kubectl set subject](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_subject/)
        + [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/)
        + [kubectl top](/docs/reference/kubectl/generated/kubectl_top/)
          - [kubectl top node](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/)
          - [kubectl top pod](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/)
        + [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/)
        + [kubectl version](/docs/reference/kubectl/generated/kubectl_version/)
        + [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/)
      * [kubectl Commands](/docs/reference/kubectl/kubectl-cmds/)
      * [kubectl](/docs/reference/kubectl/kubectl/)
      * [JSONPath Support](/docs/reference/kubectl/jsonpath/)
      * [kubectl for Docker Users](/docs/reference/kubectl/docker-cli-to-kubectl/)
      * [kubectl Usage Conventions](/docs/reference/kubectl/conventions/)
      * [Kubectl user preferences (kuberc)](/docs/reference/kubectl/kuberc/)
    - [Encodings](/docs/reference/encodings/)
      * [KYAML Reference](/docs/reference/encodings/kyaml/)
    - [Component tools](/docs/reference/command-line-tools-reference/)
      * [Feature Gates](/docs/reference/command-line-tools-reference/feature-gates/)
      * [Feature Gates (removed)](/docs/reference/command-line-tools-reference/feature-gates-removed/)
      * [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/)
      * [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/)
      * [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
      * [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/)
      * [kubelet](/docs/reference/command-line-tools-reference/kubelet/)
    - [Debug cluster](/docs/reference/debug-cluster/)
      * [Flow control](/docs/reference/debug-cluster/flow-control/)
    - [Configuration APIs](/docs/reference/config-api/)
      * [Client Authentication (v1)](/docs/reference/config-api/client-authentication.v1/)
      * [Client Authentication (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/)
      * [Event Rate Limit Configuration (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
      * [Image Policy API (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)
      * [kube-apiserver Admission (v1)](/docs/reference/config-api/apiserver-admission.v1/)
      * [kube-apiserver Audit Configuration (v1)](/docs/reference/config-api/apiserver-audit.v1/)
      * [kube-apiserver Configuration (v1)](/docs/reference/config-api/apiserver-config.v1/)
      * [kube-apiserver Configuration (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/)
      * [kube-apiserver Configuration (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/)
      * [kube-controller-manager Configuration (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
      * [kube-proxy Configuration (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
      * [kube-scheduler Configuration (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
      * [kubeadm Configuration (v1beta3)](/docs/reference/config-api/kubeadm-config.v1beta3/)
      * [kubeadm Configuration (v1beta4)](/docs/reference/config-api/kubeadm-config.v1beta4/)
      * [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)
      * [Kubelet Configuration (v1)](/docs/reference/config-api/kubelet-config.v1/)
      * [Kubelet Configuration (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/)
      * [Kubelet Configuration (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/)
      * [Kubelet CredentialProvider (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)
      * [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/)
      * [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)
      * [WebhookAdmission Configuration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)
    - [External APIs](/docs/reference/external-api/)
      * [Kubernetes Custom Metrics (v1beta2)](/docs/reference/external-api/custom-metrics.v1beta2/)
      * [Kubernetes External Metrics (v1beta1)](/docs/reference/external-api/external-metrics.v1beta1/)
      * [Kubernetes Metrics (v1beta1)](/docs/reference/external-api/metrics.v1beta1/)
    - [Scheduling](/docs/reference/scheduling/)
      * [Scheduler Configuration](/docs/reference/scheduling/config/)
      * [Scheduling Policies](/docs/reference/scheduling/policies/)
    - [Other Tools](/docs/reference/tools/)
  + [Contribute](/docs/contribute/ "Contribute to Kubernetes")
    - [Contribute to Kubernetes Documentation](/docs/contribute/docs/)
    - [Contributing to Kubernetes blogs](/docs/contribute/blog/)
      * [Submitting articles to Kubernetes blogs](/docs/contribute/blog/article-submission/)
      * [Blog guidelines](/docs/contribute/blog/guidelines/)
      * [Blog article mirroring](/docs/contribute/blog/article-mirroring/)
      * [Post-release communications](/docs/contribute/blog/release-comms/)
      * [Helping as a blog writing buddy](/docs/contribute/blog/writing-buddy/)
    - [Suggesting content improvements](/docs/contribute/suggesting-improvements/)
    - [Contributing new content](/docs/contribute/new-content/)
      * [Opening a pull request](/docs/contribute/new-content/open-a-pr/)
      * [Previewing locally](/docs/contribute/new-content/preview-locally/)
      * [Documenting for a release](/docs/contribute/new-content/new-features/ "Documenting a feature for a release")
      * [Case studies](/docs/contribute/new-content/case-studies/ "Submitting case studies")
    - [Reviewing changes](/docs/contribute/review/)
      * [Reviewing pull requests](/docs/contribute/review/reviewing-prs/)
      * [For approvers and reviewers](/docs/contribute/review/for-approvers/ "Reviewing for approvers and reviewers")
    - [Localizing Kubernetes documentation](/docs/contribute/localization/)
    - [Participating in SIG Docs](/docs/contribute/participate/)
      * [Roles and responsibilities](/docs/contribute/participate/roles-and-responsibilities/)
      * [Issue Wranglers](/docs/contribute/participate/issue-wrangler/)
      * [PR wranglers](/docs/contribute/participate/pr-wranglers/)
    - [Documentation style overview](/docs/contribute/style/)
      * [Content guide](/docs/contribute/style/content-guide/ "Documentation Content Guide")
      * [Style guide](/docs/contribute/style/style-guide/ "Documentation Style Guide")
      * [Diagram guide](/docs/contribute/style/diagram-guide/ "Diagram Guide")
      * [Writing a new topic](/docs/contribute/style/write-new-topic/)
      * [Page content types](/docs/contribute/style/page-content-types/)
      * [Content organization](/docs/contribute/style/content-organization/)
      * [Custom Hugo Shortcodes](/docs/contribute/style/hugo-shortcodes/)
    - [Updating Reference Documentation](/docs/contribute/generate-ref-docs/)
      * [Quickstart](/docs/contribute/generate-ref-docs/quickstart/ "Reference Documentation Quickstart")
      * [Contributing to the Upstream Kubernetes Code](/docs/contribute/generate-ref-docs/contribute-upstream/)
      * [Generating Reference Documentation for the Kubernetes API](/docs/contribute/generate-ref-docs/kubernetes-api/)
      * [Generating Reference Documentation for kubectl Commands](/docs/contribute/generate-ref-docs/kubectl/)
      * [Generating Reference Documentation for Metrics](/docs/contribute/generate-ref-docs/metrics-reference/)
      * [Generating Reference Pages for Kubernetes Components and Tools](/docs/contribute/generate-ref-docs/kubernetes-components/)
    - [Advanced contributing](/docs/contribute/advanced/)
    - [Viewing Site Analytics](/docs/contribute/analytics/)
  + [Docs smoke test page](/docs/test/)

[StatefulSet API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
 [Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/workloads/controllers/statefulset.md)
 [Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/workloads/controllers/statefulset.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)
 [Create an issue](https://github.com/kubernetes/website/issues/new?title=StatefulSets)
 [Print entire section](https://kubernetes.io/docs/concepts/workloads/controllers/_print/)

* [Using StatefulSets](#using-statefulsets)
* [Limitations](#limitations)
* [Components](#components)
  + [Pod Selector](#pod-selector)
  + [Volume Claim Templates](#volume-claim-templates)
  + [Minimum ready seconds](#minimum-ready-seconds)
* [Pod Identity](#pod-identity)
  + [Ordinal Index](#ordinal-index)
  + [Start ordinal](#start-ordinal)
  + [Stable Network ID](#stable-network-id)
  + [Stable Storage](#stable-storage)
  + [Pod Name Label](#pod-name-label)
  + [Pod index label](#pod-index-label)
* [Deployment and Scaling Guarantees](#deployment-and-scaling-guarantees)
  + [Pod Management Policies](#pod-management-policies)
* [Update strategies](#update-strategies)
* [Rolling Updates](#rolling-updates)
  + [Partitioned rolling updates](#partitions)
  + [Maximum unavailable Pods](#maximum-unavailable-pods)
  + [Forced rollback](#forced-rollback)
* [Revision history](#revision-history)
  + [How StatefulSets track changes using ControllerRevisions](#how-statefulsets-track-changes-using-controllerrevisions)
  + [Managing Revision History](#managing-revision-history)
* [PersistentVolumeClaim retention](#persistentvolumeclaim-retention)
  + [Replicas](#replicas)
* [What's next](#what-s-next)

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Workloads](https://kubernetes.io/docs/concepts/workloads/)
4. [Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/)
5. [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

# StatefulSets

A StatefulSet runs a group of Pods, and maintains a sticky identity for each of those Pods. This is useful for managing applications that need persistent storage or a stable, unique network identity.

StatefulSet is the workload API object used to manage stateful applications.

Manages the deployment and scaling of a set of [Pods](/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), *and provides guarantees about the ordering and uniqueness* of these Pods.

Like a [Deployment](/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."), a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.

If you want to use storage volumes to provide persistence for your workload, you can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet are susceptible to failure, the persistent Pod identifiers make it easier to match existing volumes to the new Pods that replace any that have failed.

## Using StatefulSets

StatefulSets are valuable for applications that require one or more of the
following:

* Stable, unique network identifiers.
* Stable, persistent storage.
* Ordered, graceful deployment and scaling.
* Ordered, automated rolling updates.

In the above, stable is synonymous with persistence across Pod (re)scheduling.
If an application doesn't require any stable identifiers or ordered deployment,
deletion, or scaling, you should deploy your application using a workload object
that provides a set of stateless replicas.
[Deployment](/docs/concepts/workloads/controllers/deployment/) or
[ReplicaSet](/docs/concepts/workloads/controllers/replicaset/) may be better suited to your stateless needs.

## Limitations

* The storage for a given Pod must either be provisioned by a
  [PersistentVolume Provisioner](/docs/concepts/storage/dynamic-provisioning/)
  based on the requested *storage class*, or pre-provisioned by an admin.
* Deleting and/or scaling a StatefulSet down will *not* delete the volumes associated with the
  StatefulSet. This is done to ensure data safety, which is generally more valuable than an
  automatic purge of all related StatefulSet resources.
* StatefulSets currently require a [Headless Service](/docs/concepts/services-networking/service/#headless-services)
  to be responsible for the network identity of the Pods. You are responsible for creating this
  Service.
* StatefulSets do not provide any guarantees on the termination of pods when a StatefulSet is
  deleted. To achieve ordered and graceful termination of the pods in the StatefulSet, it is
  possible to scale the StatefulSet down to 0 prior to deletion.
* When using [Rolling Updates](#rolling-updates) with the default
  [Pod Management Policy](#pod-management-policies) (`OrderedReady`),
  it's possible to get into a broken state that requires
  [manual intervention to repair](#forced-rollback).

## Components

The example below demonstrates the components of a StatefulSet.

```
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # by default is 1
  minReadySeconds: 10 # by default is 0
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: registry.k8s.io/nginx-slim:0.24
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "my-storage-class"
      resources:
        requests:
          storage: 1Gi
```

#### Note:

This example uses the `ReadWriteOnce` access mode, for simplicity. For
production use, the Kubernetes project recommends using the `ReadWriteOncePod`
access mode instead.

In the above example:

* A Headless Service, named `nginx`, is used to control the network domain.
* The StatefulSet, named `web`, has a Spec that indicates that 3 replicas of the nginx container will be launched in unique Pods.
* The `volumeClaimTemplates` will provide stable storage using
  [PersistentVolumes](/docs/concepts/storage/persistent-volumes/) provisioned by a
  PersistentVolume Provisioner.

The name of a StatefulSet object must be a valid
[DNS label](/docs/concepts/overview/working-with-objects/names/#dns-label-names).

### Pod Selector

You must set the `.spec.selector` field of a StatefulSet to match the labels of its
`.spec.template.metadata.labels`. Failing to specify a matching Pod Selector will result in a
validation error during StatefulSet creation.

### Volume Claim Templates

You can set the `.spec.volumeClaimTemplates` field to create a
[PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).
This will provide stable storage to the StatefulSet if either:

* The StorageClass specified for the volume claim is set up to use [dynamic
  provisioning](/docs/concepts/storage/dynamic-provisioning/).
* The cluster already contains a PersistentVolume with the correct StorageClass
  and sufficient available storage space.

### Minimum ready seconds

FEATURE STATE:
`Kubernetes v1.25 [stable]`

`.spec.minReadySeconds` is an optional field that specifies the minimum number of seconds for which a newly
created Pod should be running and ready without any of its containers crashing, for it to be considered available.
This is used to check progression of a rollout when using a [Rolling Update](#rolling-updates) strategy.
This field defaults to 0 (the Pod will be considered available as soon as it is ready). To learn more about when
a Pod is considered ready, see [Container Probes](/docs/concepts/workloads/pods/pod-lifecycle/#container-probes).

## Pod Identity

StatefulSet Pods have a unique identity that consists of an ordinal, a
stable network identity, and stable storage. The identity sticks to the Pod,
regardless of which node it's (re)scheduled on.

### Ordinal Index

For a StatefulSet with N [replicas](#replicas), each Pod in the StatefulSet
will be assigned an integer ordinal, that is unique over the Set. By default,
pods will be assigned ordinals from 0 up through N-1. The StatefulSet controller
will also add a pod label with this index: `apps.kubernetes.io/pod-index`.

### Start ordinal

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

`.spec.ordinals` is an optional field that allows you to configure the integer
ordinals assigned to each Pod. It defaults to nil. Within the field, you can
configure the following options:

* `.spec.ordinals.start`: If the `.spec.ordinals.start` field is set, Pods will
  be assigned ordinals from `.spec.ordinals.start` up through
  `.spec.ordinals.start + .spec.replicas - 1`.

### Stable Network ID

Each Pod in a StatefulSet derives its hostname from the name of the StatefulSet
and the ordinal of the Pod. The pattern for the constructed hostname
is `$(statefulset name)-$(ordinal)`. The example above will create three Pods
named `web-0,web-1,web-2`.
A StatefulSet can use a [Headless Service](/docs/concepts/services-networking/service/#headless-services)
to control the domain of its Pods. The domain managed by this Service takes the form:
`$(service name).$(namespace).svc.cluster.local`, where "cluster.local" is the
cluster domain.
As each Pod is created, it gets a matching DNS subdomain, taking the form:
`$(podname).$(governing service domain)`, where the governing service is defined
by the `serviceName` field on the StatefulSet.

Depending on how DNS is configured in your cluster, you may not be able to look up the DNS
name for a newly-run Pod immediately. This behavior can occur when other clients in the
cluster have already sent queries for the hostname of the Pod before it was created.
Negative caching (normal in DNS) means that the results of previous failed lookups are
remembered and reused, even after the Pod is running, for at least a few seconds.

If you need to discover Pods promptly after they are created, you have a few options:

* Query the Kubernetes API directly (for example, using a watch) rather than relying on DNS lookups.
* Decrease the time of caching in your Kubernetes DNS provider (typically this means editing the
  config map for CoreDNS, which currently caches for 30 seconds).

As mentioned in the [limitations](#limitations) section, you are responsible for
creating the [Headless Service](/docs/concepts/services-networking/service/#headless-services)
responsible for the network identity of the pods.

Here are some examples of choices for Cluster Domain, Service name,
StatefulSet name, and how that affects the DNS names for the StatefulSet's Pods.

| Cluster Domain | Service (ns/name) | StatefulSet (ns/name) | StatefulSet Domain | Pod DNS | Pod Hostname |
| --- | --- | --- | --- | --- | --- |
| cluster.local | default/nginx | default/web | nginx.default.svc.cluster.local | web-{0..N-1}.nginx.default.svc.cluster.local | web-{0..N-1} |
| cluster.local | foo/nginx | foo/web | nginx.foo.svc.cluster.local | web-{0..N-1}.nginx.foo.svc.cluster.local | web-{0..N-1} |
| kube.local | foo/nginx | foo/web | nginx.foo.svc.kube.local | web-{0..N-1}.nginx.foo.svc.kube.local | web-{0..N-1} |

#### Note:

Cluster Domain will be set to `cluster.local` unless
[otherwise configured](/docs/concepts/services-networking/dns-pod-service/).

### Stable Storage

For each VolumeClaimTemplate entry defined in a StatefulSet, each Pod receives one
PersistentVolumeClaim. In the nginx example above, each Pod receives a single PersistentVolume
with a StorageClass of `my-storage-class` and 1 GiB of provisioned storage. If no StorageClass
is specified, then the default StorageClass will be used. When a Pod is (re)scheduled
onto a node, its `volumeMounts` mount the PersistentVolumes associated with its
PersistentVolume Claims. Note that, the PersistentVolumes associated with the
Pods' PersistentVolume Claims are not deleted when the Pods, or StatefulSet are deleted.
This must be done manually.

### Pod Name Label

When the StatefulSet [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") creates a Pod,
it adds a label, `statefulset.kubernetes.io/pod-name`, that is set to the name of
the Pod. This label allows you to attach a Service to a specific Pod in
the StatefulSet.

### Pod index label

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

When the StatefulSet [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") creates a Pod,
the new Pod is labelled with `apps.kubernetes.io/pod-index`. The value of this label is the ordinal index of
the Pod. This label allows you to route traffic to a particular pod index, filter logs/metrics
using the pod index label, and more. Note the feature gate `PodIndexLabel` is enabled and locked by default for this
feature, in order to disable it, users will have to use server emulated version v1.31.

## Deployment and Scaling Guarantees

* For a StatefulSet with N replicas, when Pods are being deployed, they are created sequentially, in order from {0..N-1}.
* When Pods are being deleted, they are terminated in reverse order, from {N-1..0}.
* Before a scaling operation is applied to a Pod, all of its predecessors must be Running and Ready. If [`.spec.minReadySeconds`](#minimum-ready-seconds) is set, predecessors must be available (Ready for at least `minReadySeconds`).
* Before a Pod is terminated, all of its successors must be completely shutdown.

The StatefulSet should not specify a `pod.Spec.TerminationGracePeriodSeconds` of 0. This practice
is unsafe and strongly discouraged. For further explanation, please refer to
[force deleting StatefulSet Pods](/docs/tasks/run-application/force-delete-stateful-set-pod/).

When the nginx example above is created, three Pods will be deployed in the order
web-0, web-1, web-2. web-1 will not be deployed before web-0 is
[Running and Ready](/docs/concepts/workloads/pods/pod-lifecycle/), and web-2 will not be deployed until
web-1 is Running and Ready. If web-0 should fail, after web-1 is Running and Ready, but before
web-2 is launched, web-2 will not be launched until web-0 is successfully relaunched and
becomes Running and Ready.

If a user were to scale the deployed example by patching the StatefulSet such that
`replicas=1`, web-2 would be terminated first. web-1 would not be terminated until web-2
is fully shutdown and deleted. If web-0 were to fail after web-2 has been terminated and
is completely shutdown, but prior to web-1's termination, web-1 would not be terminated
until web-0 is Running and Ready.

### Pod Management Policies

StatefulSet allows you to relax its ordering guarantees while
preserving its uniqueness and identity guarantees via its `.spec.podManagementPolicy` field.

#### OrderedReady Pod Management

`OrderedReady` pod management is the default for StatefulSets. It implements the behavior
described in [Deployment and Scaling Guarantees](#deployment-and-scaling-guarantees).

#### Parallel Pod Management

`Parallel` pod management tells the StatefulSet controller to launch or
terminate all Pods in parallel, and to not wait for Pods to become Running
and Ready or completely terminated prior to launching or terminating another
Pod.

For scaling operations, this means all Pods are created or terminated simultaneously.

For rolling updates when [`.spec.updateStrategy.rollingUpdate.maxUnavailable`](#maximum-unavailable-pods)
is greater than 1, the StatefulSet controller terminates and creates up to `maxUnavailable` Pods
simultaneously (also known as "bursting"). This can speed up updates but may result in Pods becoming ready out of order, which might not be suitable for applications requiring strict ordering.

## Update strategies

A StatefulSet's `.spec.updateStrategy` field allows you to configure
and disable automated rolling updates for containers, labels, resource request/limits, and
annotations for the Pods in a StatefulSet. There are two possible values:

`OnDelete`
:   When a StatefulSet's `.spec.updateStrategy.type` is set to `OnDelete`,
    the StatefulSet controller will not automatically update the Pods in a
    StatefulSet. Users must manually delete Pods to cause the controller to
    create new Pods that reflect modifications made to a StatefulSet's `.spec.template`.

`RollingUpdate`
:   The `RollingUpdate` update strategy implements automated, rolling updates for the Pods in a
    StatefulSet. This is the default update strategy.

## Rolling Updates

When a StatefulSet's `.spec.updateStrategy.type` is set to `RollingUpdate`, the
StatefulSet controller will delete and recreate each Pod in the StatefulSet. It will proceed
in the same order as Pod termination (from the largest ordinal to the smallest), updating
each Pod one at a time.

The Kubernetes control plane waits until an updated Pod is Running and Ready prior
to updating its predecessor. If you have set `.spec.minReadySeconds` (see
[Minimum Ready Seconds](#minimum-ready-seconds)), the control plane additionally waits that
amount of time after the Pod turns ready, before moving on.

### Partitioned rolling updates

The `RollingUpdate` update strategy can be partitioned, by specifying a
`.spec.updateStrategy.rollingUpdate.partition`. If a partition is specified, all Pods with an
ordinal that is greater than or equal to the partition will be updated when the StatefulSet's
`.spec.template` is updated. All Pods with an ordinal that is less than the partition will not
be updated, and, even if they are deleted, they will be recreated at the previous version. If a
StatefulSet's `.spec.updateStrategy.rollingUpdate.partition` is greater than its `.spec.replicas`,
updates to its `.spec.template` will not be propagated to its Pods.
In most cases you will not need to use a partition, but they are useful if you want to stage an
update, roll out a canary, or perform a phased roll out.

### Maximum unavailable Pods

FEATURE STATE:
`Kubernetes v1.35 [beta]`

You can control the maximum number of Pods that can be unavailable during an update
by specifying the `.spec.updateStrategy.rollingUpdate.maxUnavailable` field.
The value can be an absolute number (for example, `5`) or a percentage of desired
Pods (for example, `10%`). Absolute number is calculated from the percentage value
by rounding it up. This field cannot be 0. The default setting is 1.

This field applies to all Pods in the range `0` to `replicas - 1`. If there is any
unavailable Pod in the range `0` to `replicas - 1`, it will be counted towards
`maxUnavailable`.

#### Note:

The `maxUnavailable` field is in Beta stage and it is enabled by default.

### Forced rollback

When using [Rolling Updates](#rolling-updates) with the default
[Pod Management Policy](#pod-management-policies) (`OrderedReady`),
it's possible to get into a broken state that requires manual intervention to repair.

If you update the Pod template to a configuration that never becomes Running and
Ready (for example, due to a bad binary or application-level configuration error),
StatefulSet will stop the rollout and wait.

In this state, it's not enough to revert the Pod template to a good configuration.
Due to a [known issue](https://github.com/kubernetes/kubernetes/issues/67250),
StatefulSet will continue to wait for the broken Pod to become Ready
(which never happens) before it will attempt to revert it back to the working
configuration.

After reverting the template, you must also delete any Pods that StatefulSet had
already attempted to run with the bad configuration.
StatefulSet will then begin to recreate the Pods using the reverted template.

## Revision history

ControllerRevision is a Kubernetes API resource used by controllers, such as the StatefulSet controller, to track historical configuration changes.

StatefulSets use ControllerRevisions to maintain a revision history, enabling rollbacks and version tracking.

### How StatefulSets track changes using ControllerRevisions

When you update a StatefulSet's Pod template (`spec.template`), the StatefulSet controller:

1. Prepares a new ControllerRevision object
2. Stores a snapshot of the Pod template and metadata
3. Assigns an incremental revision number

#### Key Properties

See [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/) to learn more about key properties and other details.

---

### Managing Revision History

Control retained revisions with `.spec.revisionHistoryLimit`:

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: webapp
spec:
  revisionHistoryLimit: 5  # Keep last 5 revisions
  # ... other spec fields ...
```

* **Default**: 10 revisions retained if unspecified
* **Cleanup**: Oldest revisions are garbage-collected when exceeding the limit

#### Performing Rollbacks

You can revert to a previous configuration using:

```
# View revision history
kubectl rollout history statefulset/webapp

# Rollback to a specific revision
kubectl rollout undo statefulset/webapp --to-revision=3
```

This will:

* Apply the Pod template from revision 3
* Create a new ControllerRevision with an updated revision number

#### Inspecting ControllerRevisions

To view associated ControllerRevisions:

```
# List all revisions for the StatefulSet
kubectl get controllerrevisions -l app.kubernetes.io/name=webapp

# View detailed configuration of a specific revision
kubectl get controllerrevision/webapp-3 -o yaml
```

#### Best Practices

##### Retention Policy

* Set `revisionHistoryLimit` between **5–10** for most workloads.
* Increase only if **deep rollback history** is required.

##### Monitoring

* Regularly check revisions with:

  ```
  kubectl get controllerrevisions
  ```

* Alert on **rapid revision count growth**.

##### Avoid

* Manual edits to ControllerRevision objects.
* Using revisions as a backup mechanism (use actual backup tools).
* Setting `revisionHistoryLimit: 0` (disables rollback capability).

## PersistentVolumeClaim retention

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

The optional `.spec.persistentVolumeClaimRetentionPolicy` field controls if
and how PVCs are deleted during the lifecycle of a StatefulSet. You must enable the
`StatefulSetAutoDeletePVC` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
on the API server and the controller manager to use this field.
Once enabled, there are two policies you can configure for each StatefulSet:

`whenDeleted`
:   Configures the volume retention behavior that applies when the StatefulSet is deleted.

`whenScaled`
:   Configures the volume retention behavior that applies when the replica count of
    the StatefulSet is reduced; for example, when scaling down the set.

For each policy that you can configure, you can set the value to either `Delete` or `Retain`.

`Delete`
:   The PVCs created from the StatefulSet `volumeClaimTemplate` are deleted for each Pod
    affected by the policy. With the `whenDeleted` policy all PVCs from the
    `volumeClaimTemplate` are deleted after their Pods have been deleted. With the
    `whenScaled` policy, only PVCs corresponding to Pod replicas being scaled down are
    deleted, after their Pods have been deleted.

`Retain` (default)
:   PVCs from the `volumeClaimTemplate` are not affected when their Pod is
    deleted. This is the behavior before this new feature.

Bear in mind that these policies **only** apply when Pods are being removed due to the
StatefulSet being deleted or scaled down. For example, if a Pod associated with a StatefulSet
fails due to node failure, and the control plane creates a replacement Pod, the StatefulSet
retains the existing PVC. The existing volume is unaffected, and the cluster will attach it to
the node where the new Pod is about to launch.

The default for policies is `Retain`, matching the StatefulSet behavior before this new feature.

Here is an example policy:

```
apiVersion: apps/v1
kind: StatefulSet
...
spec:
  persistentVolumeClaimRetentionPolicy:
    whenDeleted: Retain
    whenScaled: Delete
...
```

The StatefulSet [controller](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") adds
[owner references](/docs/concepts/overview/working-with-objects/owners-dependents/#owner-references-in-object-specifications)
to its PVCs, which are then deleted by the [garbage collector](/docs/concepts/architecture/garbage-collection/ "A collective term for the various mechanisms Kubernetes uses to clean up cluster resources.") after the Pod is terminated. This enables the Pod to
cleanly unmount all volumes before the PVCs are deleted (and before the backing PV and
volume are deleted, depending on the retain policy). When you set the `whenDeleted`
policy to `Delete`, an owner reference to the StatefulSet instance is placed on all PVCs
associated with that StatefulSet.

The `whenScaled` policy must delete PVCs only when a Pod is scaled down, and not when a
Pod is deleted for another reason. When reconciling, the StatefulSet controller compares
its desired replica count to the actual Pods present on the cluster. Any StatefulSet Pod
whose id greater than the replica count is condemned and marked for deletion. If the
`whenScaled` policy is `Delete`, the condemned Pods are first set as owners to the
associated StatefulSet template PVCs, before the Pod is deleted. This causes the PVCs
to be garbage collected after only the condemned Pods have terminated.

This means that if the controller crashes and restarts, no Pod will be deleted before its
owner reference has been updated appropriate to the policy. If a condemned Pod is
force-deleted while the controller is down, the owner reference may or may not have been
set up, depending on when the controller crashed. It may take several reconcile loops to
update the owner references, so some condemned Pods may have set up owner references and
others may not. For this reason we recommend waiting for the controller to come back up,
which will verify owner references before terminating Pods. If that is not possible, the
operator should verify the owner references on PVCs to ensure the expected objects are
deleted when Pods are force-deleted.

### Replicas

`.spec.replicas` is an optional field that specifies the number of desired Pods. It defaults to 1.

Should you manually scale a StatefulSet, via `kubectl scale statefulset statefulset --replicas=X`, and then you update that StatefulSet
based on a manifest (for example: by running `kubectl apply -f statefulset.yaml`), then applying that manifest overwrites the manual scaling
that you previously did.

If a [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
(or any similar API for horizontal scaling) is managing scaling for a
Statefulset, don't set `.spec.replicas`. Instead, allow the Kubernetes
[control plane](/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") to manage
the `.spec.replicas` field automatically.

## What's next

* Learn about [Pods](/docs/concepts/workloads/pods/).
* Find out how to use StatefulSets
  + Follow an example of [deploying a stateful application](/docs/tutorials/stateful-application/basic-stateful-set/).
  + Follow an example of [deploying Cassandra with Stateful Sets](/docs/tutorials/stateful-application/cassandra/).
  + Follow an example of [running a replicated stateful application](/docs/tasks/run-application/run-replicated-stateful-application/).
  + Learn how to [scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/).
  + Learn what's involved when you [delete a StatefulSet](/docs/tasks/run-application/delete-stateful-set/).
  + Learn how to [configure a Pod to use a volume for storage](/docs/tasks/configure-pod-container/configure-volume-storage/).
  + Learn how to [configure a Pod to use a PersistentVolume for storage](/docs/tutorials/configuration/configure-persistent-volume-storage/).
* `StatefulSet` is a top-level resource in the Kubernetes REST API.
  Read the
  [StatefulSet](/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
  object definition to understand the API for stateful sets.
* Read about [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) and how
  you can use it to manage application availability during disruptions.

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

  

Last modified March 16, 2026 at 12:28 PM PST: [updated other reference links (281dd818cd)](https://github.com/kubernetes/website/commit/281dd818cdd4297f452f174a35c86e3ead5aba2c)

© 2026 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/LICENSE)

© 2026 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP license: 京ICP备17074266号-3